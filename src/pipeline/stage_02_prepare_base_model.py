from src.config.configuration import ConfigurationManager
from src.components.Prepare_Base_Model import BaseModel
from src import logger

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    def PrepareBaseModelPipeline(self):
        config = ConfigurationManager()
        base_model_config = config.get_base_model_config()
        base_model = BaseModel(base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()

stage_name2="Prepare Base Model"   
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {stage_name2} started <<<<<<")

        obj = PrepareBaseModelTrainingPipeline()
        obj.PrepareBaseModelPipeline()

        logger.info(
            f">>>>>> stage {stage_name2} completed <<<<<<\n\nx==========x"
        )
    except Exception as e:
        logger.error(f"stage {stage_name2} failed")
        raise e   