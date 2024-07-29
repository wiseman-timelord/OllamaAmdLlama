# scripts/gradio_interface.py

import gradio as gr
import os
import yaml
import logging
from scripts.model_handler import load_model, unload_model, serve_model
from scripts.processing_manager import BINARY_PATHS

logger = logging.getLogger(__name__)

# Load configuration from YAML
def load_config():
    with open('./data/general_settings.yaml', 'r') as file:
        return yaml.safe_load(file)

# Save configuration to YAML
def save_config(config):
    with open('./data/general_settings.yaml', 'w') as file:
        yaml.dump(config, file)

# Global state to keep track of the loaded model and processing options
current_model_info = {"filename": None, "size": None, "loaded": False}
config = load_config()

def get_model_info(file_path):
    """Get model information based on the file path."""
    if not os.path.isfile(file_path):
        return {"filename": None, "size": None, "loaded": False}
    
    size = os.path.getsize(file_path)
    filename = os.path.basename(file_path)
    
    return {"filename": filename, "size": size, "loaded": False}

def select_model(file_path):
    """Select and display model information."""
    global current_model_info
    current_model_info = get_model_info(file_path)
    config['models']['default'] = file_path
    save_config(config)
    logger.info(f"Selected model: {current_model_info['filename']}")
    return update_model_info_display()

def load_selected_model():
    """Load the selected model."""
    global current_model_info
    if current_model_info["filename"] is None:
        return "No model selected."
    
    model_path = config['models']['default']
    load_model(model_path)
    current_model_info["loaded"] = True
    logger.info(f"Loaded model: {model_path}")
    return update_model_info_display()

def unload_selected_model():
    """Unload the selected model."""
    global current_model_info
    if not current_model_info["loaded"]:
        return "No model is currently loaded."

    unload_model()
    current_model_info["loaded"] = False
    logger.info(f"Unloaded model: {current_model_info['filename']}")
    return update_model_info_display()

def toggle_processing_option():
    """Toggle between available processing methods."""
    options = list(BINARY_PATHS.keys())
    current_option = config['processing']['option']
    new_index = (options.index(current_option) + 1) % len(options)
    new_option = options[new_index]
    config['processing']['option'] = new_option
    save_config(config)
    logger.info(f"Processing option set to: {new_option}")
    return update_processing_info_display()

def update_model_info_display():
    """Return a string representation of the current model info."""
    status = "Loaded" if current_model_info["loaded"] else "Unloaded"
    model_info = f"Filename: {current_model_info['filename']}\nSize: {current_model_info['size']} bytes\nStatus: {status}"
    return model_info

def update_processing_info_display():
    """Return a string representation of the current processing option."""
    return f"Processing: {config['processing']['option']}"

def serve_selected_model():
    """Serve the selected model to applications."""
    if not current_model_info["loaded"]:
        return "Model must be loaded before serving."
    serve_model()
    return "Model is being served."

def create_interface():
    """Create and launch the Gradio interface."""
    model_info_textbox = gr.Textbox(value=update_model_info_display(), label="Model Information", interactive=False)
    processing_info_textbox = gr.Textbox(value=update_processing_info_display(), label="Processing Method", interactive=False)
    
    # Create interface
    with gr.Blocks() as interface:
        # First Row
        with gr.Row():
            model_info_textbox.render()

        # Second Row
        with gr.Row():
            processing_info_textbox.render()
            gr.Button("Toggle Processing", elem_id="toggle_processing").click(
                toggle_processing_option,
                outputs=[processing_info_textbox]
            )
        
        # Third Row
        with gr.Row():
            gr.Button("Browse", elem_id="browse_button").click(
                select_model, inputs=gr.File(label="Select Model File", type="file"), outputs=[model_info_textbox]
            )
            gr.Button("Load", elem_id="load_button").click(
                load_selected_model, outputs=[model_info_textbox]
            )
            gr.Button("Unload", elem_id="unload_button").click(
                unload_selected_model, outputs=[model_info_textbox]
            )
            gr.Button("Serve", elem_id="serve_button").click(
                serve_selected_model, outputs=[model_info_textbox]
            )
            gr.Button("Exit", elem_id="exit_button").click(
                lambda: os._exit(0)
            )

    return interface

def launch_interface():
    interface = create_interface()
    interface.launch()

if __name__ == "__main__":
    launch_interface()
