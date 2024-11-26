# Import necessary modules
from hate.config.configuration import ConfigurationManager
from hate.components.data_transforamation import DataTransformation
from hate.logger import logging

# Constants
STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self, config_manager: ConfigurationManager = ConfigurationManager):
        self.config_manager = config_manager()

    def run(self):
        try:
            logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

            # Fetch the required configurations and artifacts
            data_transformation_config = self.config_manager.get_data  # Updated line
            data_ingestion_artifacts = self.config_manager.get_data_ingestion_artifacts()

            # Pass both configurations to DataTransformation
            data_transformation = DataTransformation(
                data_transformation_config=data_transformation_config,
                data_ingestion_artifacts=data_ingestion_artifacts
            )

            # Run the transformation
            data_transformation_artifact = data_transformation.transform_data()

            logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
            return data_transformation_artifact

        except Exception as e:
            logging.exception(e)
            raise e

if __name__ == '__main__':
    pipeline = DataTransformationPipeline()
    pipeline.run()
