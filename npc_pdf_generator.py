import json
import os
from jinja2 import Template
from weasyprint import HTML
import logging
import dotenv
import argparse
from tqdm_loggable.auto import tqdm
from tqdm_loggable.tqdm_logging import tqdm_logging

# Determine base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load environment variables
dotenv.load_dotenv(os.path.join(base_dir, '.env'))

DEFAULT_ERROR_LEVEL = logging.ERROR

# Define a custom logging level for silent mode
SILENT = 60
logging.addLevelName(SILENT, 'SILENT')

def logging_name_to_int_level(level_name):
    return getattr(logging, level_name.upper(), DEFAULT_ERROR_LEVEL)
    

def configure_logging(level_name):
    level = logging_name_to_int_level(level_name)
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')
    tqdm_logging.set_level(level)

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
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate NPC PDFs from JSON data and an HTML template.')
    parser.add_argument('--npc_data_file', type=str, help='Path to the NPC data JSON file')
    parser.add_argument('--html_template_file', type=str, help='Path to the HTML template file')
    parser.add_argument('--output_directory', type=str, help='Directory to output the generated PDF files')
    parser.add_argument('--logging_level', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', 'SILENT'], help='Set the logging level')
    args = parser.parse_args()

    # Load configuration
    config = {
        "npc_data_file": args.npc_data_file or os.path.join(base_dir, os.getenv('NPC_DATA_FILE')),
        "html_template_file": args.html_template_file or os.path.join(base_dir, os.getenv('HTML_TEMPLATE_FILE')),
        "output_directory": args.output_directory or os.path.join(base_dir, os.getenv('OUTPUT_DIRECTORY')),
        "logging_level": args.logging_level or os.getenv('LOGGING_LEVEL', 'ERROR')
    }

    # Configure logging
    configure_logging(config['logging_level'])

    # Ensure output directory exists
    os.makedirs(config['output_directory'], exist_ok=True)

    # Check if the required files exist
    if not os.path.isfile(config['npc_data_file']):
        logging.error(f"NPC data file not found: {config['npc_data_file']}")
        return
    
    if not os.path.isfile(config['html_template_file']):
        logging.error(f"HTML template file not found: {config['html_template_file']}")
        return
    
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
    for npc in (tqdm(npc_data, desc="Generating PDFs", unit="npc") if (args.logging_level or os.getenv('LOGGING_LEVEL', 'INFO')) != 'SILENT' else npc_data):
        pdf_file = generate_npc_pdf(npc, template_content, config['output_directory'])
        if pdf_file:
            pdf_files.append(pdf_file)
    
    if pdf_files:
        logging.info(f"Generated PDF files: {pdf_files}")
    else:
        logging.error("No PDF files were generated.")

if __name__ == "__main__":
    main()