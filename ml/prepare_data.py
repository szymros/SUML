"""
This module is responsible for preparing and preprocessing the dataset
for the machine learning model.
It includes data cleaning, outlier removal, encoding of categorical features,
and saving the processed dataset.
"""

import json

import pandas as pd

from config.config import (FEATURES, MAPPING_PATH, PREPARED_DATASET_PATH,
                           RAW_DATASET_PATH)


def prepare_data():
    dataset = pd.read_csv(RAW_DATASET_PATH)
    dataset = dataset[FEATURES]

    # clean data
    dataset.dropna(inplace=True)

    # remove outliers
    describe = dataset.describe(percentiles=[0.1, 0.9])
    dataset = dataset[
        (dataset["mileage"] > describe["mileage"]["10%"])
        & (dataset["mileage"] < describe["mileage"]["90%"])
        ]
    dataset = dataset[
        (dataset["vol_engine"] > describe["vol_engine"]["10%"])
        & (dataset["vol_engine"] < describe["vol_engine"]["90%"])
        ]
    dataset = dataset[
        (dataset["year"] > describe["year"]["10%"])
        & (dataset["year"] < describe["year"]["90%"])
        ]
    dataset = dataset[dataset["fuel"] != "CNG"]

    # encode categorical features
    mark_categories = dataset["mark"].unique()
    mark_cat_mapping = {mark_categories[i]: i for i in range(len(mark_categories))}
    dataset["mark"] = dataset["mark"].map(mark_cat_mapping)

    fuel_categories = dataset["fuel"].unique()
    fuel_cat_mapping = {fuel_categories[i]: i for i in range(len(fuel_categories))}
    dataset["fuel"] = dataset["fuel"].map(fuel_cat_mapping)

    # save prepared dataset
    dataset.to_csv(PREPARED_DATASET_PATH, index=False)

    # save mappings
    mappings = {"mark": mark_cat_mapping, "fuel": fuel_cat_mapping}
    json.dump(mappings, open(MAPPING_PATH, "w"))

    return dataset


if __name__ == "__main__":
    prepare_data()
