
import json
import os
from jinja2 import Template
from weasyprint import HTML
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration
config = {
    "npc_data_file": "/mnt/data/NPCs_to_PDF/npcs_updated.json",
    "html_template_file": "/mnt/data/NPCs_to_PDF/npc_template.html",
    "output_directory": "/mnt/data/NPCs_to_PDF/output"
}

# Ensure output directory exists
os.makedirs(config['output_directory'], exist_ok=True)

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error loading JSON file {file_path}: {e}")
        return None

def load_template(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error loading HTML template {file_path}: {e}")
        return None

def validate_npc_data(npc_data):
    required_fields = ["name", "role", "appearance", "race", "class", "age", "personality", "quirks", "stat_block"]
    for npc in npc_data:
        for field in required_fields:
            if field not in npc:
                logging.error(f"NPC data missing required field: {field}")
                return False
    return True

def generate_npc_pdf(npc, template_content, output_dir):
    try:
        template = Template(template_content)
        html_content = template.render(npc)
        html_file_path = os.path.join(output_dir, f"{npc['name'].replace(' ', '_')}.html")
        pdf_file_path = os.path.join(output_dir, f"{npc['name'].replace(' ', '_')}.pdf")
        
        with open(html_file_path, "w") as file:
            file.write(html_content)
        
        HTML(string=html_content).write_pdf(pdf_file_path)
        return pdf_file_path
    except Exception as e:
        logging.error(f"Error generating PDF for {npc['name']}: {e}")
        return None

def main():
    npc_data = load_json(config['npc_data_file'])
    if npc_data is None:
        logging.error("Failed to load NPC data.")
        return
    
    if not validate_npc_data(npc_data):
        logging.error("NPC data validation failed.")
        return
    
    template_content = load_template(config['html_template_file'])
    if template_content is None:
        logging.error("Failed to load HTML template.")
        return
    
    pdf_files = []
    for npc in npc_data:
        pdf_file = generate_npc_pdf(npc, template_content, config['output_directory'])
        if pdf_file:
            pdf_files.append(pdf_file)
    
    if pdf_files:
        logging.info(f"Generated PDF files: {pdf_files}")
    else:
        logging.error("No PDF files were generated.")

if __name__ == "__main__":
    main()
