# These are like tools we import from other parts of the system that we need to use in this part of the code.
from hate.constants import *
import os
from hate.utils.common import read_yaml, create_directories, save_json
from hate.entity.config_entity import DataIngestionConfig

# This is a special class (like a template) that helps manage how the system gets its settings.
class ConfigurationManager:
    # This function runs when we first create or start using this manager. It sets everything up.
    def __init__(self, config_filepath = CONFIG_FILE_PATH):
        # Here we are opening a settings file (imagine it's like reading a letter that tells you how to set up something) 
        # and storing the information from that file to use later.
        self.config = read_yaml(config_filepath)
      
        # Based on what we read from the file, we make sure all necessary folders are created for the system.
        create_directories([self.config.artifacts_root])

    # This function is specifically for getting the settings related to bringing data into the system.
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Here we are pulling out the part of the settings that tell us how the data should be brought into the system.
        config = self.config.data_ingestion

        # We make sure that the folder where the data will be stored is created.
        create_directories([config.root_dir])

        # Now we organize the data ingestion settings (like the place from where the data should come, 
        # the location where it will be saved, etc.) so it's easy for the system to understand and use.
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,        # Where the data will go.
            source_URL=config.source_URL,    # Where the data will come from.
            local_data_file=config.local_data_file,  # The file where data will be stored locally.
            unzip_dir=config.unzip_dir      # Where the data will be extracted (if it's in a compressed format).
        )

        # Finally, we return this organized information so it can be used in the system to process the data.
        return data_ingestion_config
