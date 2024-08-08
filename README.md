
# NPC PDF Generator

## Overview

This project generates PDF files for NPCs (Non-Player Characters) based on JSON data and an HTML template. It uses Jinja2 for templating and WeasyPrint for PDF generation.

## Files

- `generate_npc_pdfs_improved.py`: The main script to generate PDFs.
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
pip install jinja2 weasyprint
```

## Usage

1. Place the NPC JSON data file (`npcs_updated.json`) and the HTML template file (`npc_template.html`) in the same directory as the script.
2. Run the script:

```bash
python generate_npc_pdfs_improved.py
```

3. The generated PDF files will be saved in the `output/` directory.

## Example

The sample JSON data includes one NPC, "Aria Windrunner". The script will generate a PDF for this NPC.
