import streamlit as st
import joblib

st.title("House Price Predictor")

# Load the trained model
model = joblib.load("src/model.pkl")

# User input for the 3 features
RM = st.number_input("Average number of rooms (RM)", min_value=1.0, max_value=10.0, value=6.0)
LSTAT = st.number_input("Lower status of the population (%) (LSTAT)", min_value=0.0, max_value=40.0, value=12.0)
PTRATIO = st.number_input("Pupil-teacher ratio (PTRATIO)", min_value=1.0, max_value=30.0, value=15.0)

# Predict
if st.button("Predict Price"):
    prediction = model.predict([[RM, LSTAT, PTRATIO]])
    st.write(f"Predicted House Price: ${prediction[0]:,.2f}")
