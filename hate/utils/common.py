import os
from box.exceptions import BoxValueError
import yaml
from hate import logger
import json
import joblib
from ensure import ensure_annotations  # type: ignore
from box import ConfigBox
from pathlib import Path
from typing import Any, List
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns as ConfigBox.

    Args:
        path_to_yaml (Path): Path to YAML file.

    Raises:
        ValueError: If YAML file is empty.
        FileNotFoundError: If the file does not exist.
        Exception: For other generic issues.

    Returns:
        ConfigBox: Parsed YAML data.
    """
    try:
        if not path_to_yaml.exists():
            raise FileNotFoundError(f"YAML file not found at: {path_to_yaml}")
        
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file) or {}
            if not content:
                raise BoxValueError("YAML file is empty")
            logger.info(f"YAML file loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        logger.error(f"Error reading YAML file at {path_to_yaml}: {e}")
        raise

@ensure_annotations
def create_directories(path_to_directories: List[Path], verbose=True):
    """Create list of directories.

    Args:
        path_to_directories (List[Path]): List of directory paths.
        verbose (bool, optional): Log directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save dictionary data to JSON file.

    Args:
        path (Path): Path to save JSON file.
        data (dict): Data to be saved in JSON format.
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"JSON file saved at: {path}")
    except TypeError as e:
        logger.error(f"Data provided to save_json is not serializable: {e}")
        raise
    except Exception as e:
        logger.error(f"Error saving JSON file at {path}: {e}")
        raise

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load JSON file and return as ConfigBox.

    Args:
        path (Path): Path to JSON file.

    Returns:
        ConfigBox: Parsed JSON data.
    """
    try:
        with open(path) as f:
            content = json.load(f)
        logger.info(f"JSON file loaded successfully from: {path}")
        return ConfigBox(content)
    except FileNotFoundError:
        logger.error(f"JSON file not found at: {path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON at {path}: {e}")
        raise

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save data as binary file using joblib.

    Args:
        data (Any): Data to save.
        path (Path): Path to save binary file.
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at: {path}")
    except Exception as e:
        logger.error(f"Error saving binary file at {path}: {e}")
        raise

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary data from file.

    Args:
        path (Path): Path to binary file.

    Returns:
        Any: Loaded binary data.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded from: {path}")
        return data
    except FileNotFoundError:
        logger.error(f"Binary file not found at: {path}")
        raise
    except Exception as e:
        logger.error(f"Error loading binary file at {path}: {e}")
        raise

@ensure_annotations
def get_size(path: Path) -> str:
    """Get file size in KB.

    Args:
        path (Path): Path to file.

    Returns:
        str: File size in KB.
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~ {size_in_kb} KB"
    except FileNotFoundError:
        logger.error(f"File not found for size check at: {path}")
        raise
