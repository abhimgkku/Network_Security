import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

class NetworkDataExtractFromMongo():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def export_collection_as_dataframe(self,database_name,collection_name):
        try:
            self.database_name = database_name
            self.collection_name = collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[self.database_name][self.collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.tolist():
                df = df.drop(columns=["_id"],axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
if __name__ == '__main__':
    FILE_PATH="./Network_Data/NetworkData.csv"
    DATABASE="NetworkDataBase"
    COLLECTION="NetworkDataCollection"
    data_extract = NetworkDataExtractFromMongo()
    dataframe = data_extract.export_collection_as_dataframe(database_name=DATABASE,collection_name=COLLECTION)
    print(dataframe)