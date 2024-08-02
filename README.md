# GoStudlyAmdLlamas!
Through Gradio interfaced, LM Studio and Ollama , emulation utilizing llama.cpp pre-compilled binaries for, Vulkan and avx2 and avx512.

## DESCRIPTION:
Due to a lack of AMD compatibility for hosting models on gpu, I determined the time had come for a solution to the issue; the GoStudlyAmdLlamas! program is designed to manage and serve language models using various processing options, tailored towards AMD hardware, the problem is most software is designed for nVidia, limiting AMD users to the yes more, but slower processing of most of ones processor. It offers both a REST API and a Gradio-based GUI to interact with the system, making it versatile for different use cases. The GoStudlyAmdLlamas! program provides a comprehensive solution for managing and serving language models on Windows. By utilizing pre-compiled binaries for different processing capabilities, it offers flexibility in performance optimization. The program supports  graphical user interface, making it accessible for various uses and applications.

### FEATURES:
- Interactive Gui : User-friendly interface with Gradio, requiring no command-line input.
- Model Management : Serve models through ollama compatible internal server.
- Processing Options : Toggle processing methods (none, avx, avx2, vulkan) via the GUI.
- Configuration Persistence : Changes to settings are saved in general_settings.yaml


## DEVELOPMENT:
GoStudlyAmdLlamas! implementation still in alpha stage, it is considererd not working.
- requires basic development.
- requires testing for stability.
- interactions with other programs needs testing.

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
    ├── exampleFolder/              # Directories for llama.cpp binaries
    │   └── llama-cli.exe           # Binary for llama.cpp
```
