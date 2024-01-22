"""Main script for running the data preparation and model training pipeline for this project."""

from ml.prepare_data import prepare_data
from ml.train_model import model_pipeline

if __name__ == "__main__":
    prepare_data()
    model_pipeline()
