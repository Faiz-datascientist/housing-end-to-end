import os 
import sys #system error
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation

@dataclass
class Dataingestionconfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw_data.csv")


#create a class for data ingestion
class dataIngestion:
    def __init__(self):
        self.ingestion_config=Dataingestionconfig() #ingestion_config is variable

    def initiate_data_config(self):
        logging.info("data ingestion method starts")

        try:
            df=pd.read_csv(r"E:\DATA SETS\gemstone\gemstone.csv")
            logging.info("dataset read file successfully")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("train test split start")
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=41)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("data ingestion is completed!!!! ")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e:
            logging.info("Exception occured in data ingestion part")
            raise CustomException(e,sys)
        
        




