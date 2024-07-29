# main_script.py

import yaml
import logging
from scripts.processing_manager import initialize_processing
from scripts.gradio_interface import launch_interface

def load_config():
    with open('./data/general_settings.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()

    # Set up logging
    logging.basicConfig(level=config['logging']['level'])
    logger = logging.getLogger(__name__)
    logger.info("Starting OhLlamas!")

    # Initialize Processing
    initialize_processing(config['processing'])

    # Launch Gradio interface
    launch_interface()

if __name__ == "__main__":
    main()
