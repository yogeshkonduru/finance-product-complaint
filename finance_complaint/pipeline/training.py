import os,sys
from finance_complaint.logger import logger
from finance_complaint.exception import FinanceException
from finance_complaint.config.pipeline.training import FinanceConfig
from finance_complaint.component import DataIngestion



class TrainingPipeline:
    def __init__(self,finance_config: FinanceConfig):
        self.finance_config = finance_config
    
    def start_data_ingestion(self):
        try:
            data_ingestion_config = self.finance_config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
            data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise FinanceException(e, sys)

    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise FinanceException(e, sys)

    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise FinanceException(e, sys)

    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise FinanceException(e, sys)

    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise FinanceException(e, sys)

    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise FinanceException(e, sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise FinanceException(e, sys)

