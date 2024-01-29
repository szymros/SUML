# SUML

# About
This project is centered around the development of a machine learning model that aims to accurately predict the prices of cars. Our model uses car brand, fuel type, year of manufacture, mileage, and engine volume, to make its predictions. Model is based on data from a well-known polish car sale site.

# Usage
The easiest way to use this app is to run the binary file or open it in streamlit cloud [link].

Second approach:

**1. Clone the Frontend Branch**: First, clone the frontend branch of our project, which includes all necessary files.

**2. Open and Run**: Open the project in your IDE or navigate to the project directory using the command line. Install all of the required packages. Then, run the application by entering streamlit run app.py.

**3. Input and Predict**: In the Streamlit interface, input the car details such as brand, fuel type, year, mileage, and engine volume. The model will then display the predicted price.

# Deployment for Windows and Linux

**1. Clone the Frontend Branch**: First, clone the frontend branch of our project, which includes all necessary files.

**2. Install the necessary packages**: Install packages provided in requirements.txt file.

**3. Provide local machine paths**: In run_app.spec file provide local machine paths to python library and path to app code.

**4. Run pyinstaller**: Run the following command to create the binary: pyinstaller run_app.spec --clean 

Python 3.10.9

# Dataset 
https://www.kaggle.com/datasets/aleksandrglotov/car-prices-poland
