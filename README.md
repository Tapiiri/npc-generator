
# NPC PDF Generator

## Overview

This project generates PDF files for NPCs (Non-Player Characters) based on JSON data and an HTML template. It uses Jinja2 for templating and WeasyPrint for PDF generation.

## Files

- `npc_pdf_generator.py`: The main script to generate PDFs.
- `npcs_updated.json`: Sample JSON data for NPCs.
- `npc_template.html`: HTML template for rendering NPC data.
- `output/`: Directory where the generated PDF files will be saved.

## Requirements

- Python 3.x
- Jinja2
- WeasyPrint

## Setup

1. Ensure you have Python 3.x installed.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```
3. Copy `.env.example` file and rename the copy to `.env`.

4. Reconfigure the file locations in `.env` as necessary.

## Usage

1. Keep the NPC JSON data file (`npcs_updated.json`) and the HTML template file (`npc_template.html`) in the location defined in `.env`. For sample use, the locations are preconfigured.

2. Run the script:

```bash
python npc_pdf_generator.py
```

3. The generated PDF files will be saved in the `output/` directory (or the folder you reconfigured in the `.env` file).

## Example

The sample JSON data includes some sample NPCs. The script will generate PDFs for them. [An example is displayed here.](Aria%20Windrunned.pdf)

## License

MIT. 

Enjoy!

