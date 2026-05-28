import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('model.pkl')

# Title
st.title("Ford Car Price Prediction")

# User inputs
year = st.number_input("Car Year")
mileage = st.number_input("Mileage")
engine_size = st.number_input("Engine Size")

# Prediction button
if st.button("Predict Price"):

    features = np.array([[year, mileage, engine_size]])

    prediction = model.predict(features)

    st.success(f"Predicted Price: £{prediction[0]:,.2f}")
