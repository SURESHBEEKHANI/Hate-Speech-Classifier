# Importing necessary modules
import logging  # Provides functionality for logging messages to a file or console
import os  # Provides functions for interacting with the operating system, such as file paths
from from_root import from_root  # Utility to find the root of the project directory (custom module)
from datetime import datetime  # Provides functions to handle date and time

# Creating a unique log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Constructing the full path to the 'logs' directory, appending the log file name
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the 'logs' directory if it does not exist, ensuring the folder structure is in place
os.makedirs(logs_path, exist_ok=True)

# Define the final log file path by joining the logs path with the log file name
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Log messages will be saved to this file
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",  # Format for log messages (timestamp, logger name, log level, message)
    level=logging.DEBUG,  # Set the minimum logging level to DEBUG (captures all levels: DEBUG, INFO, WARNING, ERROR, CRITICAL)
)
