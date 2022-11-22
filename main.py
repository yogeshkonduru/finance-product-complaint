import os,sys
from finance_complaint.constant.environment.variable_key import AWS_ACCESS_KEY_ID_ENV_KEY,AWS_SECRET_ACCESS_KEY_ENV_KEY
from dotenv import load_dotenv
load_dotenv()
access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY, )
secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY, )
# print(access_key_id,secret_access_key)
from finance_complaint.logger import logger
from finance_complaint.exception import FinanceException
from finance_complaint.pipeline import TrainingPipeline
from finance_complaint.config.pipeline.training import FinanceConfig

def main():
    try:
        finance_config = FinanceConfig()
        training_pipeline = TrainingPipeline(finance_config)
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logger.info(FinanceException(e,sys))

if __name__=="__main__":
    main()