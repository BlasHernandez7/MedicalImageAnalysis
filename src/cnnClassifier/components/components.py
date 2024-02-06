from src.cnnClassifier.entity.config_entity import DataIngestionEntity
import opendatasets as od


class DataIngestionComponent:
    def __init__(self,
                 dataIngestionConfig=DataIngestionEntity):
        self.dataPath = dataIngestionConfig.local_data_file
        self.dataURL = dataIngestionConfig.source_URL
        
    def data_download(self):
        od.download_kaggle_dataset(data_dir=self.dataPath,
                           dataset_url=self.dataURL)