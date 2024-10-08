import os
from dotenv import load_dotenv

class Config:
    def __init__(self, args):
        # Load environment variables
        base_dir = os.path.dirname(os.path.abspath(__file__))
        load_dotenv(os.path.join(base_dir, '.env'))

        # Set configuration variables
        self.base_dir = base_dir
        self.npc_data_file = args.npc_data_file or os.getenv('NPC_DATA_FILE')
        self.output_directory = args.output_directory or os.getenv('OUTPUT_DIRECTORY', os.path.join(base_dir, 'output'))
        self.logging_level = args.logging_level or os.getenv('LOGGING_LEVEL', 'ERROR')

        # Ensure output directory exists
        os.makedirs(self.output_directory, exist_ok=True)
