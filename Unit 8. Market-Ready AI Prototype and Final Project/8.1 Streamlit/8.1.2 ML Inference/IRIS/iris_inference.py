# Simple Streamlit web app for ML inference on the Iris dataset
import streamlit as st
import joblib

# Load the trained KNN model
loaded_classifier = joblib.load('knn_model.pkl')

st.title('Iris Flower Classification')
st.write('This is a simple Streamlit app for classifying Iris flowers.')

# Input features from the user
sepal_length = st.number_input('Sepal Length (cm)', min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input('Sepal Width (cm)', min_value=0.0, max_value=10.0, value=3.0)
petal_length = st.number_input('Petal Length (cm)', min_value=0.0, max_value=10.0, value=1.0)
petal_width = st.number_input('Petal Width (cm)', min_value=0.0, max_value=10.0, value=0.2) 

# Create a feature array for prediction
features = [[sepal_length, sepal_width, petal_length, petal_width]]

# Add a button to trigger the prediction
if st.button('Predict'):
    # Make a prediction
    prediction = loaded_classifier.predict(features)
    st.write(f'Predicted class: {prediction[0]}')  

# streamlit run iris_inference.py