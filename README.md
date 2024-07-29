# OhLlamas!
Ollama emulation through llama.cpp pre-compilled binaries and gradio.

## DESCRIPTION:
The OhLlamas! program is designed to manage and serve language models using various processing options. It offers both a REST API and a Gradio-based GUI to interact with the system, making it versatile for different use cases. The OhLlamas! program provides a comprehensive solution for managing and serving language models on Windows. By utilizing pre-compiled binaries for different processing capabilities, it offers flexibility in performance optimization. The program supports both command-line and graphical user interfaces, making it accessible for various users and applications.

### FEATURES:
- Interactive Gui : User-friendly interface with Gradio, requiring no command-line input.
- Model Management : Serve models through ollama compatible internal server.
- Processing Options : Toggle processing methods (none, avx, avx2, vulkan) via the GUI.
- Configuration Persistence : Changes to settings are saved in general_settings.yaml


## DEVELOPMENT:
OhLlamas! implementation still in alpha stage, it is considererd not working.

### STRUCTURES:
- The current file structures...
```
OhLlamas!/
│
├── main_script.py                  # Main entry point for the application
│
├── data/
│   └── general_settings.yaml       # Configuration file for server, model, and processing settings
│
├── scripts/
│   ├── __init__.py                 # Initialization file for the scripts package
│   ├── model_handler.py            # Handles model loading, unloading, and serving
│   ├── processing_manager.py       # Manages the selection of processing binaries
│   └── gradio_interface.py         # Creates and manages the Gradio GUI
│
└── libraries/
    ├── none/                       # Directory for 'none' processing binaries
    │   └── llama-cli.exe           # Binary for basic CPU processing
    │
    ├── avx/                        # Directory for 'avx' processing binaries
    │   └── llama-cli.exe           # Binary for AVX CPU processing
    │
    ├── avx2/                       # Directory for 'avx2' processing binaries
    │   └── llama-cli.exe           # Binary for AVX2 CPU processing
    │
    └── vulkan/                     # Directory for 'vulkan' processing binaries
        └── llama-cli.exe           # Binary for Vulkan GPU processing
```
