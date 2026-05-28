import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load('model.pkl')

# Load feature names
feature_names = joblib.load('feature_names.pkl')

# Title
st.title("Ford Car Price Prediction")

# User Inputs
year = st.number_input("Car Year", min_value=2000, max_value=2030, step=1)
mileage = st.number_input("Mileage", min_value=0)
engine_size = st.number_input("Engine Size", min_value=0.0, step=0.1)

# Predict Button
if st.button("Predict Price"):

    # Create empty dataframe with same columns used during training
    input_data = pd.DataFrame(columns=feature_names)

    # Fill all columns with 0
    input_data.loc[0] = 0

    # Add user inputs
    input_data['year'] = year
    input_data['mileage'] = mileage
    input_data['engineSize'] = engine_size

    # Prediction
    prediction = model.predict(input_data)

    # Show result
    st.success(f"Predicted Price: £{prediction[0]:,.2f}")
