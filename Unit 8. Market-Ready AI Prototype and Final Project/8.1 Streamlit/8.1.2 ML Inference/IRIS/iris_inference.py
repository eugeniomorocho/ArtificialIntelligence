# pip install streamlit
import streamlit as st

st.title("Iris Flower Species Prediction")
st.write("Enter the measurements of the Iris flower to predict its species.")

# Load the trained model
import joblib
model = joblib.load("knn_model.pkl")

# Create input fields for the user to enter the measurements
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.0)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=4.0)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=1.0)

# Create a button to trigger the prediction
if st.button("Predict Species"):
    # Prepare the input data for prediction
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    # Display the predicted species
    st.write(f"The predicted species is: {prediction[0]}")

# streamlit run iris_inference.py