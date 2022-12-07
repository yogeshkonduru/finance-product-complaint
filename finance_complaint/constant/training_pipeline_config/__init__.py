import os

PIPELINE_NAME = "finance-complaint"
PIPELINE_ARTIFACT_DIR = os.path.join(os.getcwd(), "finance_artifact")

from finance_complaint.constant.training_pipeline_config.data_ingestion import *
from finance_complaint.constant.training_pipeline_config.data_validation import *