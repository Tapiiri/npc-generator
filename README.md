# NPC Generator

_ReadMe Generated with ChatGPT-o1 - except AI funkiness!_
## Overview

The **NPC Generator** is a Python-based tool designed to create detailed PDF character sheets for Non-Player Characters (NPCs) in role-playing games like Dungeons & Dragons. It leverages a flexible data model defined in JSON, modular HTML templates with Jinja2 templating, and WeasyPrint for PDF generation. The system is built to be extensible, allowing for easy customization of data fields, templates, and layouts.

## Features

- **Flexible Data Model**: Supports a wide range of NPC attributes, stat blocks, custom fields, and metadata, defined in a JSON schema.
- **Modular Templates**: Uses component-based HTML templates that can be customized and extended.
- **Dynamic Rendering**: Generates NPC sheets based on data and template instructions, allowing for different layouts and sections.
- **Extensibility**: Easily add new templates, data fields, or output formats without significant code changes.
- **Command-Line Interface**: Provides a CLI for generating PDFs with options to specify data files, output directories, and logging levels.
- **Data Validation**: Validates NPC data against a JSON schema to ensure data integrity.

## Table of Contents

- [Directory Structure](#directory-structure)
- [Dependencies](#dependencies)
- [Setup](#setup)
- [Usage](#usage)
  - [Command-Line Arguments](#command-line-arguments)
  - [Environment Variables](#environment-variables)
- [Data Model](#data-model)
  - [Sample NPC Data](#sample-npc-data)
- [Templates](#templates)
  - [Customizing Templates](#customizing-templates)
- [Directory Structure](#directory-structure)
- [Customization](#customization)
- [License](#license)
- [Contributing](#contributing)

## Directory Structure

```
npc_generator/
├── main.py
├── config.py
├── logger.py
├── data_loader.py
├── template_renderer.py
├── output_generator.py
├── validators.py
├── npc_schema.json
├── requirements.txt
├── .env
├── templates/
│   ├── base.html
│   ├── detailed.html
│   ├── components/
│   │   ├── attributes.html
│   │   ├── stat_block.html
│   │   ├── custom_fields.html
│   │   ├── metadata.html
│   │   ├── macros.html
│   └── styles.css
├── data/
│   └── npc_data.json
└── output/
```

- **`main.py`**: Entry point of the application.
- **`config.py`**: Handles configuration loading and management.
- **`logger.py`**: Sets up logging.
- **`data_loader.py`**: Loads and validates NPC data.
- **`template_renderer.py`**: Handles template rendering.
- **`output_generator.py`**: Manages output generation (HTML, PDF).
- **`validators.py`**: Contains validation functions and schema loading.
- **`npc_schema.json`**: JSON schema for validating NPC data.
- **`templates/`**: Contains base templates and components.
- **`data/`**: Directory for NPC data files.
- **`output/`**: Directory where generated files are saved.

## Dependencies

- **Python 3.x**
- **Jinja2**: Templating engine.
- **WeasyPrint**: For generating PDFs from HTML and CSS.
- **jsonschema**: For validating JSON data against a schema.
- **python-dotenv**: For loading environment variables from a `.env` file.
- **tqdm** (optional): For progress bars in the CLI.

Install dependencies using:

```bash
pip install -r requirements.txt
```

**System Dependencies for WeasyPrint**:

WeasyPrint may require additional system libraries:

- **Cairo**
- **Pango**
- **GDK-PixBuf**
- **Libffi**

On Ubuntu/Debian:

```bash
sudo apt-get install libpango1.0-0 libpangocairo-1.0-0 libcairo2 libcairo2-dev libffi-dev shared-mime-info
```

Refer to the [WeasyPrint documentation](https://weasyprint.readthedocs.io/en/latest/install.html#linux) for detailed installation instructions.

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/npc_generator.git
   cd npc_generator
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**:

   Copy the example `.env` file and modify it as needed.

   ```bash
   cp .env.example .env
   ```

   **`.env` File Contents**:

   ```ini
   # .env

   # Path to your NPC data JSON file
   NPC_DATA_FILE=data/npc_data.json

   # Directory to output the generated files
   OUTPUT_DIRECTORY=output

   # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
   LOGGING_LEVEL=INFO
   ```

5. **Ensure the Directory Structure**:

   Make sure the `data/` directory contains your NPC data JSON file (`npc_data.json`), and the `templates/` directory contains all the necessary template files.

## Usage

Run the main script to generate NPC PDFs:

```bash
python main.py
```

The generated HTML and PDF files will be saved in the `output/` directory (or the directory specified in your `.env` file).

### Command-Line Arguments

The script supports command-line arguments to override configurations:

- `--npc_data_file`: Path to the NPC data JSON file.
- `--output_directory`: Directory to output the generated files.
- `--logging_level`: Set the logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

**Example**:

```bash
python main.py --npc_data_file="data/my_npcs.json" --output_directory="output" --logging_level="DEBUG"
```

### Environment Variables

You can also configure the script using environment variables set in the `.env` file:

- `NPC_DATA_FILE`: Path to the NPC data JSON file.
- `OUTPUT_DIRECTORY`: Directory to output the generated files.
- `LOGGING_LEVEL`: Set the logging level.

## Data Model

The NPC Generator uses a flexible JSON schema to define NPC data. This allows for customizable and extensible NPC character sheets.

### Key Components

- **metadata**: Contains meta-information about the NPC data.
- **attributes**: Core descriptive data about the NPC.
- **stat_blocks**: Statistical data, which can include multiple stat blocks.
- **custom_fields**: User-defined data for additional customization.
- **template_instructions**: Guides how the data should be rendered.

### Sample NPC Data

Here's an example of NPC data in `data/npc_data.json`:

```json
[
  {
    "metadata": {
      "version": "1.0",
      "author": "Dungeon Master",
      "created_at": "2023-10-05T12:34:56Z",
      "notes": "Key NPC for the upcoming quest arc."
    },
    "attributes": {
      "name": "Arlyn the Veiled",
      "role": "Master of Magical Concealment",
      "appearance": "A middle-aged elf with piercing green eyes and long, silver hair...",
      "race": "Elf",
      "class": "Wizard",
      "age": 145,
      "personality": "Calm, analytical, and somewhat aloof...",
      "quirks": "Frequently adjusts her robes...",
      "alignment": "Neutral Good",
      "background": "Arlyn has been safeguarding the hideout...",
      "additional_info": {
        "affiliations": ["Arcane Circle", "Guardians of the Veil"],
        "notable_items": ["Veil of Shadows", "Amulet of the Hidden Path"],
        "family": {
          "mother": "Elara the Wise",
          "father": "Thalion the Swift",
          "siblings": ["Eldrin", "Lyra"]
        }
      }
    },
    "stat_blocks": [
      {
        "title": "Primary Stat Block",
        "abilities": {
          "strength": 10,
          "dexterity": 14,
          "constitution": 12,
          "intelligence": 18,
          "wisdom": 14,
          "charisma": 12
        },
        "armor_class": 12,
        "hit_points": 55,
        "speed": "30 ft.",
        "skills": ["Arcana +9", "Insight +7", "Perception +7"],
        "senses": "Darkvision 60 ft., Passive Perception 17",
        "languages": ["Common", "Elvish", "Draconic", "Sylvan"],
        "challenge_rating": 7,
        "special_abilities": [
          {
            "name": "Spellcasting",
            "description": "Arlyn is a 12th-level spellcaster...",
            "metadata": {
              "spell_list": ["Fireball", "Invisibility", "Counterspell"]
            }
          },
          {
            "name": "Arcane Ward",
            "description": "Arlyn can create a magical ward that absorbs damage...",
            "metadata": {
              "activation": "Reaction",
              "duration": "Until depleted"
            }
          }
        ]
      },
      {
        "title": "Alternate Form",
        "abilities": {
          "strength": 12,
          "dexterity": 16,
          "constitution": 14,
          "intelligence": 18,
          "wisdom": 14,
          "charisma": 14
        },
        "armor_class": 14,
        "hit_points": 65,
        "speed": "40 ft.",
        "skills": ["Stealth +9", "Arcana +9"],
        "senses": "Darkvision 60 ft., Passive Perception 17",
        "languages": ["Common", "Elvish"],
        "challenge_rating": 8,
        "special_abilities": [
          {
            "name": "Shadow Step",
            "description": "Arlyn can teleport between shadows...",
            "metadata": {
              "range": "60 ft.",
              "activation": "Bonus Action"
            }
          }
        ]
      }
    ],
    "custom_fields": {
      "motivation": "Protect the hideout and further her understanding of illusion magic.",
      "secrets": "Has a hidden agenda to find the lost Tome of Mirrors.",
      "allies": ["Council of Mages", "Shadow Enclave"],
      "enemies": ["Order of the Silver Flame", "The Whispering Tyrant"]
    },
    "template_instructions": {
      "layout": "detailed",
      "sections": ["attributes", "stat_blocks", "custom_fields", "metadata"],
      "field_formatting": {
        "name": { "display_name": "NPC Name", "location": "header" },
        "role": { "display_name": "Role/Title", "location": "header" },
        "abilities": { "format": "table", "location": "stat_block" },
        "special_abilities": { "format": "accordion", "location": "stat_block" },
        "metadata": { "display": true }
      }
    }
  }
]
```

## Templates

The NPC Generator uses Jinja2 templates located in the `templates/` directory. The templates are modular and component-based, making it easy to customize the output.

### Template Files

- **`base.html`**: The base template that defines the overall structure.
- **`detailed.html`**: Extends `base.html` and includes components based on `template_instructions`.
- **Components (`templates/components/`)**:
  - **`attributes.html`**: Renders the NPC's attributes.
  - **`stat_block.html`**: Renders stat blocks.
  - **`custom_fields.html`**: Renders custom fields.
  - **`metadata.html`**: Renders metadata.
  - **`macros.html`**: Contains reusable macros for rendering.

### Customizing Templates

You can customize the templates to change the appearance and layout of the NPC sheets.

- **Modify Existing Templates**: Edit the HTML and CSS to adjust styles and structure.
- **Add New Templates**: Create new templates or components and update the `template_instructions` in your NPC data to use them.
- **Use Template Instructions**: Control which sections are included and how fields are formatted by adjusting `template_instructions` in your NPC data.

**Example**:

```json
"template_instructions": {
  "layout": "custom_layout",
  "sections": ["attributes", "stat_blocks", "custom_fields"],
  "field_formatting": {
    "abilities": { "format": "grid", "location": "sidebar" },
    "special_abilities": { "format": "list", "location": "main" }
  }
}
```

## Customization

### Adding New Fields

To add new fields to your NPC data:

1. **Update the JSON Data**: Add the new field to your NPC data in `npc_data.json`.
2. **Modify the Templates**: Edit the relevant template to include the new field.
3. **Update the Schema (Optional)**: If you want the new field to be validated, add it to `npc_schema.json`.

### Extending Functionality

- **Custom Filters**: Add custom filters in `template_renderer.py` and use them in templates.
- **Additional Output Formats**: Modify `output_generator.py` to support other formats like images or text files.
- **Plugin Architecture**: Implement a plugin system to load custom components or processors.

## License

This project is licensed under the MIT License.