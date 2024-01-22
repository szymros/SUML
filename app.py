import json
import pickle

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from config.config import MAPPING_PATH, MODEL_SAVE_PATH

mapping = json.loads(open(MAPPING_PATH, "r").read())
mark_mapping = mapping["mark"]
fuel_mapping = mapping["fuel"]

model = pickle.load(open(MODEL_SAVE_PATH, "rb"))


st.title("Car Price Prediction :car:")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    mark = st.session_state["mark"] = st.selectbox(
        "car brand", list(mark_mapping.keys())
    )
with col2:
    selected_brand = st.session_state["mark"]
    fuel = st.selectbox("fuel type", list(fuel_mapping.keys()))
with col3:
    car_year = st.selectbox("Select your car year", [i for i in range(2010, 2024)])
with col4:
    mileage = st.text_input("mileage", value="100000")
with col5:
    vol_engine = st.text_input("engine volume", max_chars=3, value="1.6")

data_point = pd.DataFrame(
    {
        "mark": [mark_mapping[mark]],
        "fuel": [fuel_mapping[fuel]],
        "vol_engine": [int(int(vol_engine.replace(".", "")) * 100)],
        "year": [int(car_year)],
        "mileage": [int(mileage)],
    }
)


def predict_price(model, data_point):
    prediction = model.predict(data_point)
    return int(prediction)


if st.button("Predict price"):
    st.info(f"Your car price is: {predict_price(model, data_point)} PLN")
    years = {}
    for i in range(data_point["year"][0] - 2, data_point["year"][0] + 2):
        df_copy = data_point.copy()
        df_copy["year"] = [i]
        years[str(i)] = predict_price(model, df_copy)

    bar_colors = ["tab:blue", "tab:blue", "tab:red", "tab:blue", "tab:blue"]
    fig, ax1 = plt.subplots()
    ax1.bar(
        years.keys(),
        years.values(),
        color=bar_colors,
    )
    ax1.set_title("Price change in the last 5 years")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Price")
    st.pyplot(fig)
