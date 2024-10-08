import logging

def setup_logging(level_name):
    level = getattr(logging, level_name.upper(), logging.ERROR)
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')
