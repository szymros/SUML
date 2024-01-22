import pickle

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from config.config import MODEL_SAVE_PATH, PREPARED_DATASET_PATH


def get_data_set() -> tuple:
    dataset = pd.read_csv(PREPARED_DATASET_PATH)
    X = dataset.drop(columns=["price"])
    y = dataset["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test


def prepare_model(X_train, y_train) -> LinearRegression:

    lr = LinearRegression()
    print("X_train shape: ", X_train)
    lr.fit(X_train, y_train)
    pickle.dump(lr, open(MODEL_SAVE_PATH, "wb"))

    return lr


def evaluate_model(model: LinearRegression, X_test, y_test) -> tuple:
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    return score


def save_model(model: LinearRegression):
    pickle.dump(model, open(MODEL_SAVE_PATH, "wb"))


def model_pipeline():
    X_train, X_test, y_train, y_test = get_data_set()
    model = prepare_model(X_train, y_train)
    score = evaluate_model(model, X_test, y_test)
    print(f"Model r2 score: {score}")
    save_model(model)
    return score


if __name__ == "__main__":
    model_pipeline()