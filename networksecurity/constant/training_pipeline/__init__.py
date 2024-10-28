import os
import sys
import pandas as pd
import numpy as np

"""Defining common constant variables for training pipeline"""
PIPELINE_NAME: str = 'NetworkSecurity'
ARTIFACT_DIR: str = 'Artifacts'
FILE_NAME: str = 'NetworkData.csv'
TARGET_COLUMN: str = 'Result'

TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'
PREPROCESSING_OBJECT_FILE_NAME: str = 'preprocessing.pkl'
MODEL_FILE_NAME: str = 'model.pkl'
SCHEMA_FILE_PATH: str = os.path.join("data_schema","schema.yaml")
SCHEMA_DROP_COLS: str = "drop_columns"
SAVED_MODEL_DIR: str = os.path.join("saved_models")

"""Data Ingestion related constants start with DATA_INGESTION var name"""
DATA_INGESTION_COLLECTION_NAME: str =  "NetworkDataCollection"
DATA_INGESTION_DATABASE_NAME: str = "NetworkDataBase"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
"""Data Transformation related constants start with DATA_TRANSFORMATION var name"""

"""Data validation related constants start with DATA_VALIDATION var name"""

"""Model Trainer related constants start with MODEL_TRAINER var name"""