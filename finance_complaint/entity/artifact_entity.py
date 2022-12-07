from collections import namedtuple
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    metadata_file_path:str
    download_dir:str


'''
Both declarion is same and we can user any one for the artifact
'''

# DataIngestionArtifact = namedtuple("DataIngestionArtifact", ['feature_store_file_path','metadata_file_path','download_dir'])


@dataclass
class DataValidationArtifact:
    accepted_file_path:str
    rejected_dir:str

