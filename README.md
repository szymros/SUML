# SUML

# About
This project is centered around the development of a machine learning model that aims to accurately predict the prices of cars. Our model uses car brand, fuel type, year of manufacture, mileage, and engine volume, to make its predictions. Model is based on data from a well-known polish car sale site.

# Usage
The easiest way to use this app is to run it locally using the binary files located in the bin directory, which can be downloaded individually or through cloning the repository. Another is to open it in streamlit cloud [link].

Second approach:

**1. Clone the main Branch**: First, clone the main branch of our project, which includes all necessary files.

**2. Open and Run**: Open the project in your IDE or navigate to the project directory using the command line. Install all of the required packages. Then, run the application by entering streamlit run app.py.

**3. Input and Predict**: In the Streamlit interface, input the car details such as brand, fuel type, year, mileage, and engine volume. The model will then display the predicted price.

# Creating a build for Windows or Linux

**1. Clone the main Branch**: First, clone the main branch of our project, which includes all necessary files.

**2. Modify run_app.spec**: Provide local paths to system default python library and path to app code in run_app.spec file located in build folder.

**3. Compile the app**: Run build.sh script located in build folder. The compiled binary will be found in build/dist folder. For linux, make sure binutils is installed in the system before compiling.  The binary file can be freely moved to and ran in another directory.

Python 3.10.9

# Dataset 
https://www.kaggle.com/datasets/aleksandrglotov/car-prices-poland
