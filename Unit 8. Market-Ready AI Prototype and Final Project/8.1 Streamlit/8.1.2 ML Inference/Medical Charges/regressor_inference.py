# A simple Stremlit app to demonstrate the use of a trained regression model for medical charges prediction.
# %pip install streamlit (in the terminal)

import streamlit as st
import pandas as pd
import joblib

# Load the trained regression model
model = joblib.load('regression_model.pkl')

# Create the Streamlit app
st.title("Medical Charges Prediction")

# Create input fields for user to enter features
age = st.number_input("Age", min_value=0, max_value=120, value=30)
sex = st.selectbox("Sex", options=["male", "female"])
bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", options=["yes", "no"])

# Input for region selection as dummy variables with radio buttons
region = st.radio("Region", options=["northeast", "northwest", "southeast", "southwest"])

# Convert the region to dummy variables
region_northeast = 1 if region == "northeast" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# Convert categorical variables to numerical values
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0

# Make a prediction based on the user's input
if st.button("Predict"):
    # Create a DataFrame with the user's input
    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region_northeast": [region_northeast],
        "region_northwest": [region_northwest],
        "region_southeast": [region_southeast],
        "region_southwest": [region_southwest]
    })

    # Make a prediction
    prediction = model.predict(input_data)

    # Display the prediction
    st.success(f"Predicted Medical Charges: ${prediction[0]:.2f}")

# Run the app from the terminal using the command: 
# streamlit run regressor_inference.py

# Stop the app by pressing Ctrl+C in the terminal where the app is running.