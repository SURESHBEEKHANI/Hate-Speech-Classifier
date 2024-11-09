# Import necessary modules
import os  # Provides functions for interacting with the operating system, such as creating directories and checking file properties
from pathlib import Path  # Provides object-oriented file system paths
import logging  # Allows logging of events and messages

# Setting up logging configuration to display log messages at the INFO level or higher
# The format for log messages includes the timestamp and the actual log message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Defining the name of the project
project_name = "hate-speech-classification"

# List of files that need to be created along with their directory structure
# These files are defined with relative paths, which are to be created within the project structure
list_of_files = [
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transforamation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcloud_syncer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "dvc.yaml",
    ".dockerignore"
]

# Looping over each file in the list to ensure the correct directories and files exist
for filepath in list_of_files:
    # Convert the filepath to a Path object for easier manipulation
    filepath = Path(filepath)

    # Get the directory and filename from the full path
    filedir, filename = os.path.split(filepath)

    # If the directory path is not empty, create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it doesn't already exist
        logging.info(f"Creating directory; {filedir} for the file: {filename}")  # Log the directory creation

    # If the file does not exist or it is empty (size 0), create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
            logging.info(f"Creating empty file: {filepath}")  # Log that the file was created

    # If the file already exists and is non-empty, log that it's already present
    else:
        logging.info(f"{filename} already exists")  # Log that the file already exists
