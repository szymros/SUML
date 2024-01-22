"""
This module contains the functionality for training a RandomForestRegressor model
 on preprocessed car price data.
 It includes steps for data loading, model training, evaluation,
  and saving the trained model.
"""

import pickle

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from config.config import MODEL_SAVE_PATH, PREPARED_DATASET_PATH


def get_data_set() -> tuple:
    """Load and split the preprocessed dataset for model training and testing.

        Returns:
            tuple: A tuple containing split datasets: (X_train, X_test, y_train, y_test).
    """
    dataset = pd.read_csv(PREPARED_DATASET_PATH)
    X = dataset.drop(columns=["price"])
    y = dataset["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test


def prepare_model(X_train, y_train) -> RandomForestRegressor:
    """Train a RandomForestRegressor model on the training dataset.

        Args:
            X_train: Features for training.
            y_train: Target variable for training.

        Returns:
            RandomForestRegressor: The trained RandomForest model.
    """
    model = RandomForestRegressor(n_estimators=10, random_state=42)
    print("X_train shape: ", X_train)
    model.fit(X_train, y_train)
    pickle.dump(model, open(MODEL_SAVE_PATH, "wb"))

    return model


def evaluate_model(model: RandomForestRegressor, X_test, y_test) -> tuple:
    """Evaluate the performance of the trained model using the test dataset.

        Args:
            model: The trained RandomForest model.
            X_test: Features from the test dataset.
            y_test: Target variable from the test dataset.

        Returns:
            tuple: A tuple containing the R2 score of the model.
    """
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    return score


def save_model(model: RandomForestRegressor):
    """Save the trained RandomForest model to a file.

        Args:
            model: The trained RandomForest model to be saved.
    """
    pickle.dump(model, open(MODEL_SAVE_PATH, "wb"))


def model_pipeline():
    """The main pipeline for model training and evaluation.

        This function orchestrates the process of model training, evaluation,
        and saving the model.

        Returns:
            float: The R2 score of the trained model.
    """
    X_train, X_test, y_train, y_test = get_data_set()
    model = prepare_model(X_train, y_train)
    score = evaluate_model(model, X_test, y_test)
    print(f"Model r2 score: {score}, {model.score(X_test, y_test)}")
    save_model(model)
    return score


if __name__ == "__main__":
    model_pipeline()
