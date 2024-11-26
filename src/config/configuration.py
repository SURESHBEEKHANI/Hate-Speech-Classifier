from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH):
        # Load the configuration from a YAML file
        self.config = read_yaml(config_filepath)
        
        # Create the root directory for artifacts if it doesn't exist
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Retrieve the data ingestion configuration section
        ingestion_config = self.config.data_ingestion
        
        # Ensure the root directory for data ingestion exists
        create_directories([ingestion_config.root_dir])

        # Create and return a DataIngestionConfig object
        return DataIngestionConfig(
            root_dir=ingestion_config.root_dir,
            source_URL=ingestion_config.source_URL,
            local_data_file=ingestion_config.local_data_file,
            unzip_dir=ingestion_config.unzip_dir
        )
