import os 
import sys #system error
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.components.data_ingestion import dataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainner import ModelTrainer


if __name__=="__main__":
    obj=dataIngestion()
    train_data_path,test_data_path=obj.initiate_data_config()
    data_transormation=DataTransformation()
    train_arr,test_arr,_=data_transormation.initaite_data_transformation(train_data_path,test_data_path)
    model_trainner = ModelTrainer()
    model_trainner.initate_model_training(train_arr,test_arr)
    