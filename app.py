import numpy as np
import streamlit as st
import json
import pickle
from config.config import MAPPING_PATH, MODEL_SAVE_PATH
import pandas as pd


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
    car_year = st.text_input("year",max_chars=4,value="2010")
with col4:
    mileage = st.text_input("mileage",value="100000")
with col5:
    vol_engine = st.text_input("engine volume", max_chars=3,value="1.6")

data_point = pd.DataFrame({"mark": [mark_mapping[mark]], "fuel": [fuel_mapping[fuel]], "vol_engine": [int(int(vol_engine.replace(".",""))*100)], "year": [int(car_year)], "mileage": [int(mileage)]})

def predict_price(model, data_point):
    prediction = model.predict(data_point)
    return int(prediction)


if st.button("Predict price"):

    st.info(
        f"Your car price is: {predict_price(model, data_point)} PLN"
    )
