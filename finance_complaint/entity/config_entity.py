from collections import namedtuple

TrainingPipelineConfig = namedtuple('TrainingPipelineConfig',["pipeline_name","artifact_dir"])

DataIngestionConfig = namedtuple("DataIngestionConfig", ["from_date",
                                                         "to_date",
                                                         "data_ingestion_dir",
                                                         "download_dir",
                                                         "file_name",
                                                         "feature_store_dir",
                                                         "failed_dir",
                                                         "metadata_file_path",
                                                         "datasource_url"
                                                         ])

DataValidationConfig = namedtuple("DataValidationConfig", ["accepted_data_dir",
                                                           "rejected_data_dir",
                                                            "file_name"])