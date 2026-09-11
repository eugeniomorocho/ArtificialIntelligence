import streamlit as st

# Agregar título a la aplicación
st.title("🐧 Penguin Classifier")

# Importa el modelo de MLP mlp_classifier_penguins.pkl
import joblib
modelo_mlp = joblib.load("mlp_classifier_penguins.joblib")

# Agregar un encabezado para la sección de entrada de datos
st.header("Ingrese las características del pingüino")

# Agregar campos de entrada para las características del pingüino
island = st.selectbox("Isla", ["0", "1", "2"]) # 0: Biscoe, 1: Dream, 2: Torgersen
bill_length = st.number_input("Longitud del pico (mm)", min_value=0.0, step=0.1)
bill_depth = st.number_input("Profundidad del pico (mm)", min_value=0.0, step=0.1)  
flipper_length = st.number_input("Longitud del aleta (mm)", min_value=0.0, step=0.1)
body_mass = st.number_input("Masa corporal (g)", min_value=0.0, step=1.0)
sex = st.selectbox("Sexo", ["1", "2"]) 

# Realizar la predicción con el modelo de MLP
if st.button("Predecir especie"):
    # Crear un DataFrame con las características ingresadas
    import pandas as pd
    input_data = pd.DataFrame({
        "island": [island],
        "bill_length_mm": [bill_length],
        "bill_depth_mm": [bill_depth],
        "flipper_length_mm": [flipper_length],
        "body_mass_g": [body_mass],
        "sex": [sex]
    })
    # Realizar la predicción
    prediction = modelo_mlp.predict(input_data)
    # Mostrar el resultado de la predicción
    st.write(f"La especie del pingüino es: {prediction[0]}")

# Desplegar en Streamlit con el comando: streamlit run pruebaRNA.py