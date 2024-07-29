# scripts/processing_manager.py

import logging
import subprocess

logger = logging.getLogger(__name__)

BINARY_PATHS = {
    "none": "./libraries/none/llama-cli.exe",
    "avx": "./libraries/avx/llama-cli.exe",
    "avx2": "./libraries/avx2/llama-cli.exe",
    "vulkan": "./libraries/vulkan/llama-cli.exe",
}

def initialize_processing(processing_config):
    option = processing_config['option']
    binary_path = BINARY_PATHS.get(option)

    if not binary_path:
        logger.error(f"Invalid processing option: {option}")
        return

    logger.info(f"Using processing option: {option} with binary: {binary_path}")

    # Test if the binary is accessible and executable
    try:
        result = subprocess.run([binary_path, '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            logger.error(f"Error initializing binary: {result.stderr}")
        else:
            logger.info(f"Binary initialized successfully: {result.stdout}")
    except FileNotFoundError:
        logger.error(f"Binary not found at path: {binary_path}")
    except Exception as e:
        logger.error(f"An error occurred while initializing the binary: {e}")
