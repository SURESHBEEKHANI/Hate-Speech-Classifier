# Importing the necessary modules from the project
from hate.config.configuration import ConfigurationManager  # For managing system settings.
from hate.components.data_ingestion import DataIngestion  # For downloading and extracting data.
from hate.logger import logging  # For keeping track of system activities by logging messages.

# This is the name of the stage (step) in the process. In this case, it is the "Data Ingestion" stage.
STAGE_NAME = "Data Ingestion stage"

# This is a class that defines the pipeline (the sequence of steps) for the Data Ingestion process.
class DataIngestionTrainingPipeline:
    # This function is run when we create an object of this class. It's empty for now.
    def __init__(self):
        pass

    # The main function where the actual steps of the Data Ingestion process happen.
    def main(self):
        # Step 1: Get the system configuration settings from a ConfigurationManager.
        config = ConfigurationManager()
        
        # Step 2: Use those settings to get the specific configuration for Data Ingestion (getting the data into the system).
        data_ingestion_config = config.get_data_ingestion_config()
        
        # Step 3: Create an object of the DataIngestion class, which will handle the downloading and extracting of the data.
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        # Step 4: Download the data from the source.
        data_ingestion.download_file()
        
        # Step 5: Extract the downloaded data if it's in a compressed (zip) format.
        data_ingestion.extract_zip_file()

# This part ensures that the script will run when it's executed as a program (not imported elsewhere).
if __name__ == '__main__':
    try:
        # Log that the Data Ingestion stage is starting.
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Create an object of the DataIngestionTrainingPipeline class and call its main function to run the process.
        obj = DataIngestionTrainingPipeline()
        obj.main()
        
        # Log that the Data Ingestion stage is completed.
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # If there is an error, log the exception (error) details.
        logging.exception(e)
        
        # Raise the error so it can be handled elsewhere or logged further.
        raise e
