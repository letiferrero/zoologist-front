import streamlit as st
import requests

"""
# Zoologist front
"""

# Collect the penguin characteristics required by the model
island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])

# Collect the penguin's measurements
bill_length_mm = st.number_input("Bill length (mm)", value=51.9)
bill_depth_mm = st.number_input("Bill depth (mm)", value=19.5)
flipper_length_mm = st.number_input("Flipper length (mm)", value=206.0)
body_mass_g = st.number_input("Body mass (g)", value=3950.0)

# Let the user select the penguin's sex
sex = st.selectbox("Sex", ["Male", "Female"])

# Set the URL of the local prediction API
api_url = f"{st.secrets['API_URL']}/predict"

# Match each input to the query parameter expected by the API
params = {
    "island": island,
    "bill_length_mm": bill_length_mm,
    "bill_depth_mm": bill_depth_mm,
    "flipper_length_mm": flipper_length_mm,
    "body_mass_g": body_mass_g,
    "sex": sex,
}

# Send the input values to the API when the user clicks Predict
if st.button("Predict"):
    response = requests.get(api_url, params=params, timeout=10)
    prediction = response.json()["prediction"]
    st.write(f"Predicted species: {prediction}")
