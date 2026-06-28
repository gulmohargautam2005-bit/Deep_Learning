from src.config.configuration import ConfigurationManager
from src.components.model_training import Training
from src import logger


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def ModelTrainingPipeline(self):
        config=ConfigurationManager()
        training_config =config.get_training_config()
        training = Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

stage_name3="Model Training"   
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {stage_name3} started <<<<<<")

        obj = ModelTrainingPipeline()
        obj.ModelTrainingPipeline()

        logger.info(
            f">>>>>> stage {stage_name3} completed <<<<<<\n\nx==========x"
        )
    except Exception as e:
        logger.error(f"stage {stage_name3} failed")
        raise e   