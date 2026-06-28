import os
import zipfile
from src import logger  
import gdown
from src.utils.common import get_size
from src.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    def download_file(self) -> str:
        """
        Fetch data from the url
        """

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file

            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)

            if not os.path.exists(zip_download_dir):
                logger.info(
                    f"Downloading data from {dataset_url} into file {zip_download_dir}"
                )
                file_id = dataset_url.split("/")[-2]
                prefix = "https://drive.google.com/uc?export=download&id="
                gdown.download(prefix + file_id, zip_download_dir, quiet=True)
                logger.info(
                    f"Downloaded data from {dataset_url} into file {zip_download_dir}"
                )
            else:
                logger.info(
                    f"File already exists of size: {get_size(Path(zip_download_dir))}"
                )

        except Exception as e:
            raise e

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """

        unzip_path = Path(self.config.unzip_dir)
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            already_extracted = any(
                (unzip_path / f).exists() for f in zip_ref.namelist()
            )

        if already_extracted:
            print(f"Extracted files already exist at {unzip_path}, skipping...")
            return

        for file in zip_ref.namelist():
            zip_ref.extract(file, unzip_path)
