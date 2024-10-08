
import os
import logging
import shutil  # Add this import
from weasyprint import HTML

class OutputGenerator:
    def __init__(self, config, template_renderer):
        self.output_directory = config.output_directory
        self.template_renderer = template_renderer

        # Copy styles.css to output directory
        self.copy_stylesheet()

    def copy_stylesheet(self):
        stylesheet_source = os.path.join(self.template_renderer.template_dir, 'styles.css')
        stylesheet_destination = os.path.join(self.output_directory, 'styles.css')
        try:
            shutil.copyfile(stylesheet_source, stylesheet_destination)
            logging.info(f"Copied stylesheet to {stylesheet_destination}")
        except Exception as e:
            logging.error(f"Error copying stylesheet: {e}")

    def generate_outputs(self, npc_data_list):
        output_files = []
        for npc_data in npc_data_list:
            output_file = self.generate_npc_output(npc_data)
            if output_file:
                output_files.append(output_file)
        return output_files

    def generate_npc_output(self, npc_data):
        attributes = npc_data.get('attributes', {})
        name = attributes.get('name', 'Unnamed_NPC').replace(' ', '_')
        html_content = self.template_renderer.render_template(npc_data)
        if not html_content:
            return None

        html_file_path = os.path.join(self.output_directory, f"{name}.html")
        pdf_file_path = os.path.join(self.output_directory, f"{name}.pdf")

        # Set base_url to the project root directory
        base_url = self.template_renderer.template_dir

        try:
            with open(html_file_path, "w", encoding="utf-8") as file:
                file.write(html_content)
            logging.info(f"Generated HTML file at {html_file_path}")

            HTML(string=html_content, base_url=base_url).write_pdf(pdf_file_path)
            logging.info(f"Generated PDF file at {pdf_file_path}")
            return pdf_file_path
        except Exception as e:
            logging.error(f"Error generating output for {name}: {e}")
            return None
