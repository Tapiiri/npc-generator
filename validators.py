import json
import logging
import jsonschema
from jsonschema import validate

def load_schema(schema_file='npc_schema.json'):
    try:
        with open(schema_file, 'r') as file:
            schema = json.load(file)
            return schema
    except Exception as e:
        logging.error(f"Error loading JSON Schema file {schema_file}: {e}")
        return None

def validate_npc_data(npc_data):
    schema = load_schema()
    if not schema:
        return False

    validator = jsonschema.Draft7Validator(schema)
    errors = sorted(validator.iter_errors(npc_data), key=lambda e: e.path)
    if errors:
        for error in errors:
            logging.error(f"Validation error at {list(error.path)}: {error.message}")
        return False
    else:
        logging.info("NPC data validated successfully against the schema.")
        return True
