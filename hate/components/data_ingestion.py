import os
import zipfile
import gdown
from pathlib import Path  # Importing Path to handle paths as objects

from hate.logger import logging
from hate.utils.common import get_size
from hate.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        logging.info("DataIngestion class initialized with provided configuration.")

    def download_file(self) -> str:
        '''
        Fetches data from the URL defined in the configuration
        '''
        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            
            # Create directory if it does not exist
            logging.info("Creating directory for data download if it does not exist.")
            os.makedirs("artifacts/data_ingestion", exist_ok=True)

            # Log download start
            logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            # Process Google Drive download
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix + file_id, zip_download_dir)
            logging.info(f"Download completed for {zip_download_dir}")

            # Convert to Path object for get_size
            zip_download_path = Path(zip_download_dir)
            file_size = get_size(zip_download_path)  # Pass Path object instead of string
            logging.info(f"Downloaded file size: {file_size} bytes")

        except Exception as e:
            logging.error(f"Error occurred during file download: {e}")
            raise e
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir

        try:
            logging.info("Creating directory for unzipping files if it does not exist.")
            os.makedirs(unzip_path, exist_ok=True)

            logging.info(f"Extracting zip file {self.config.local_data_file} into directory {unzip_path}")
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            
            logging.info(f"Extraction completed to directory {unzip_path}")

        except zipfile.BadZipFile as e:
            logging.error(f"Failed to extract {self.config.local_data_file}: Not a valid zip file.")
            raise e

        except Exception as e:
            logging.error(f"Error occurred during file extraction: {e}")
            raise e
