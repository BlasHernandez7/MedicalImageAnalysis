from src.cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.cnnClassifier.entity.config_entity import DataIngestionEntity
from src.cnnClassifier.utils.common import create_directories, read_yaml


class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        #self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionEntity:
        
        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionEntity(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file
        )

        return data_ingestion_config
        