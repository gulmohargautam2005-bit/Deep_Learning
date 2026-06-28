from src import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
stage_name="Data Ingestion"
stage_name2="Prepare Base Model"
stage_name3="Model Training"
stage_name4="Model Evaluation"
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
    
    try:
        logger.info(f">>>>>> stage {stage_name4} started <<<<<<")

        obj = ModelEvaluationPipeline()
        obj.evaluate_model()

        logger.info(
            f">>>>>> stage {stage_name4} completed <<<<<<\n\nx==========x"
        )
    except Exception as e:
        logger.error(f"stage {stage_name4} failed")
        raise e   