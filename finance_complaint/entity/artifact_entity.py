from collections import namedtuple
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    metadata_file_path:str
    download_dir:str

# DataIngestionArtifact = namedtuple("DataIngestionArtifact", ['feature_store_file_path','metadata_file_path','download_dir'])

'''
Both declarion is same and we can user any one for the artifact
'''


