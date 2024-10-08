import argparse
import os
import sys
from logger import setup_logging
from config import Config
from data_loader import DataLoader
from template_renderer import TemplateRenderer
from output_generator import OutputGenerator

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate NPC PDFs from JSON data and templates.')
    parser.add_argument('--npc_data_file', type=str, help='Path to the NPC data JSON file')
    parser.add_argument('--output_directory', type=str, help='Directory to output the generated files')
    parser.add_argument('--logging_level', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='Set the logging level')
    args = parser.parse_args()

    # Load configuration
    config = Config(args)

    # Setup logging
    setup_logging(config.logging_level)

    # Load and validate data
    data_loader = DataLoader(config)
    npc_data = data_loader.load_and_validate_data()

    if not npc_data:
        sys.exit(1)  # Exit if data loading or validation failed

    # Initialize template renderer
    template_renderer = TemplateRenderer(config)

    # Generate outputs
    output_generator = OutputGenerator(config, template_renderer)
    output_files = output_generator.generate_outputs(npc_data)

    if output_files:
        print(f"Generated files: {output_files}")
    else:
        print("No files were generated.")

if __name__ == "__main__":
    main()
