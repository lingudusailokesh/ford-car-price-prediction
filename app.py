import streamlit as st
import joblib
import pandas as pd

# Load model and feature names
model = joblib.load('model.pkl')
feature_names = joblib.load('feature_names.pkl')

# Title
st.title("Ford Car Price Prediction")

# Numeric Inputs
year = st.number_input("Car Year", min_value=2000, max_value=2030, step=1)
mileage = st.number_input("Mileage", min_value=0)
engine_size = st.number_input("Engine Size", min_value=0.0, step=0.1)

# Categorical Inputs
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

# Prediction
if st.button("Predict Price"):

    # Create dataframe with all training columns
    input_data = pd.DataFrame(columns=feature_names)

    # Fill all values with 0
    input_data.loc[0] = 0

    # Add numerical values
    input_data['year'] = year
    input_data['mileage'] = mileage
    input_data['engineSize'] = engine_size

    # Add encoded categorical values

    model_col = 'model_' + model_name
    transmission_col = 'transmission_' + transmission
    fuel_col = 'fuelType_' + fuel_type

    # Set selected category to 1
    if model_col in input_data.columns:
        input_data[model_col] = 1

    if transmission_col in input_data.columns:
        input_data[transmission_col] = 1

    if fuel_col in input_data.columns:
        input_data[fuel_col] = 1

    # Predict
    prediction = model.predict(input_data)

    # Display result
    st.success(f"Predicted Price: £{prediction[0]:,.2f}")
