# NPC PDF Generator

## Overview

This project generates PDF files for NPCs (Non-Player Characters) based on JSON data and an HTML template. It uses Jinja2 for templating and WeasyPrint for PDF generation.

## Files

- `npc_pdf_generator.py`: The main script to generate PDFs.
- `npcs_updated.json`: Sample JSON data for NPCs.
- `npc_template.html`: HTML template for rendering NPC data.
- `output/`: Directory where the generated PDF files will be saved.

## Dependencies

- Jinja2
- WeasyPrint
- Python-dotenv
- Tqdm

## Setup

1. Ensure you have Python 3.x installed.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` file and rename the copy to `.env`.

4. Reconfigure the file locations and other settings in `.env` as necessary.

## Usage

1. Keep the NPC JSON data file (`npcs_updated.json`) and the HTML template file (`npc_template.html`) in the location defined in `.env`. For sample use, the locations are preconfigured.

2. Run the script:

```bash
python npc_pdf_generator.py
```

3. The generated PDF files will be saved in the `output/` directory (or the folder you reconfigured in the `.env` file).

### Command Line Arguments

The script supports command line arguments to override the `.env` file values:

- `--npc_data_file`: Path to the NPC data JSON file.
- `--html_template_file`: Path to the HTML template file.
- `--output_directory`: Directory to output the generated PDF files.
- `--logging_level`: Set the logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`, `SILENT`).

Example:

```bash
python npc_pdf_generator.py --npc_data_file="path/to/npcs_updated.json" --html_template_file="path/to/npc_template.html" --output_directory="path/to/output" --logging_level="DEBUG"
```

### Environment Variables

You can also configure the script using environment variables by setting them in the `.env` file:

- `NPC_DATA_FILE`: Path to the NPC data JSON file.
- `HTML_TEMPLATE_FILE`: Path to the HTML template file.
- `OUTPUT_DIRECTORY`: Directory to output the generated PDF files.
- `LOGGING_LEVEL`: Set the logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`, `SILENT`).

## Example

The sample JSON data includes some sample NPCs. The script will generate PDFs for them. [An example is displayed here.](Aria%20Windrunned.pdf)

## License

MIT. 

Enjoy!