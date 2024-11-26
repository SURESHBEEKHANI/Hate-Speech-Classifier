import os
import sys
import logging

# Define the log format string
LOG_FORMAT = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory and file paths for logging
LOG_DIR = "logs"
LOG_FILEPATH = os.path.join(LOG_DIR, "running_logs.log")

# Ensure the logging directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILEPATH),
        logging.StreamHandler(sys.stdout),
    ]
)

# Create and configure logger instance
logger = logging.getLogger("HateSpeechClassifierLogger")
