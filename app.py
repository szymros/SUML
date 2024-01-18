import streamlit as st

st.title("Car Price Prediction :car:")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.selectbox("Select your car brand", ["BMW", "Mercedes", "Toyota"])
with col2:
    st.selectbox("Select your car model", ["M3", "camry", "fds"])
with col3:
    st.selectbox("Select your car year", [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
with col4:
    st.number_input("Enter your car mileage", min_value=0, max_value=1000000, step=1000)


if st.button("Predict price"):
    st.info("Your car price is: 10000$")
