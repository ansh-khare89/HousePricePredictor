import streamlit as st
import pandas as pd
import pickle

st.title("House Price Predictor")

# Load your trained model (fixed path)
with open("src/model.pkl", "rb") as f:
    model = pickle.load(f)

# User input
bedrooms = st.number_input("Number of bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of bathrooms", min_value=1, max_value=10, value=2)
sqft = st.number_input("Square feet", min_value=100, max_value=10000, value=1000)

# Predict
if st.button("Predict Price"):
    prediction = model.predict([[bedrooms, bathrooms, sqft]])
    st.write(f"Predicted House Price: ${prediction[0]:,.2f}")
