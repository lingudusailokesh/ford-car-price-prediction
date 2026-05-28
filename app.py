import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('model.pkl')

# Load feature names
feature_names = joblib.load('feature_names.pkl')

# Title
st.title("Ford Car Price Prediction")

# Numeric Inputs
year = st.number_input("Car Year", min_value=2000, max_value=2030, step=1)

mileage = st.number_input("Mileage", min_value=0)

engine_size = st.number_input(
    "Engine Size",
    min_value=0.0,
    step=0.1
)

# Dropdown Inputs
model_name = st.selectbox(
    "Model",
    ["Fiesta", "Focus", "EcoSport", "Kuga", "Mondeo"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic", "Semi-Auto"]
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)

# Predict Button
if st.button("Predict Price"):

    # Create dataframe with SAME columns as training
    input_data = pd.DataFrame(columns=feature_names)

    # Fill all columns with 0
    input_data.loc[0] = 0

    # Add numerical features
    input_data['year'] = year
    input_data['mileage'] = mileage
    input_data['engineSize'] = engine_size

    # One-hot encoding manually

    model_column = 'model_' + model_name
    transmission_column = 'transmission_' + transmission
    fuel_column = 'fuelType_' + fuel_type

    # Set selected category to 1

    if model_column in input_data.columns:
        input_data[model_column] = 1

    if transmission_column in input_data.columns:
        input_data[transmission_column] = 1

    if fuel_column in input_data.columns:
        input_data[fuel_column] = 1

    # Prediction
    prediction = model.predict(input_data)

    # Output
    st.success(f"Predicted Price: £{prediction[0]:,.2f}")
