"""Configuration settings for the car price prediction model.

This module defines the key configuration constants used throughout the project.
It includes paths to data files, model save locations,
 and a list of features used in the model.

Attributes:
    FEATURES (list of str): List of feature names to be used in the model.
    MAPPING_PATH (str): File path for saving the mappings JSON file.
    MODEL_SAVE_PATH (str): File path for saving the trained model.
    PREPARED_DATASET_PATH (str): File path for the prepared dataset CSV file.
    RAW_DATASET_PATH (str): File path for the raw dataset CSV file.
"""

FEATURES = ["mark", "fuel", "vol_engine", "year", "mileage", "price"]
MAPPING_PATH = "./data/mappings.json"
MODEL_SAVE_PATH = "./model/model.pkl"
PREPARED_DATASET_PATH = "./data/dataset_prepared.csv"
RAW_DATASET_PATH = "./data/dataset_raw.csv"
