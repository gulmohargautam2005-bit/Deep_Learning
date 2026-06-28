from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def evaluate_model(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        model_evaluation = ModelEvaluation(evaluation_config)
        model_evaluation.evaluation()
        # model_evaluation.log_into_mlflow()

stage_name4="Model Evaluation"

if __name__ == "__main__":
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