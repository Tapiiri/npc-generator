import json
import logging
from validators import validate_npc_data

class DataLoader:
    def __init__(self, config):
        self.npc_data_file = config.npc_data_file

    def load_and_validate_data(self):
        npc_data = self.load_json()
        if npc_data and validate_npc_data(npc_data):
            return npc_data
        else:
            logging.error("Data loading or validation failed.")
            return None

    def load_json(self):
        try:
            with open(self.npc_data_file, 'r') as file:
                data = json.load(file)
                logging.info(f"Loaded NPC data from {self.npc_data_file}")
                return data
        except Exception as e:
            logging.error(f"Error loading JSON file {self.npc_data_file}: {e}")
            return None
