from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def DataIngestionPipeline(self):
        config=ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion=DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
   
stage_name="Data Ingestion"
if __name__ == "__main__": 
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")

        obj = DataIngestionTrainingPipeline()
        obj.DataIngestionPipeline()

        logger.info(
            f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x"
        )
    except Exception as e:
        logger.error(f"stage {stage_name} failed")
        raise e   

