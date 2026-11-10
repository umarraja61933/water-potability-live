import streamlit as st
import joblib
import numpy as np

# Page configuration & styling
st.set_page_config(page_title="Water Potability Predictor", page_icon="💧", layout="centered")

st.title("💧 Water Potability Prediction")
st.write("Enter the water quality parameters to check if the water is safe for drinking.")

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load('water_potability_model.pkl')

model = load_model()

# Input fields for Water Potability Features
col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
    hardness = st.number_input("Hardness", value=150.0)
    solids = st.number_input("Solids (TDS)", value=20000.0)
    chloramines = st.number_input("Chloramines", value=7.0)
    sulfate = st.number_input("Sulfate", value=300.0)

with col2:
    conductivity = st.number_input("Conductivity", value=400.0)
    organic_carbon = st.number_input("Organic Carbon", value=10.0)
    trihalomethanes = st.number_input("Trihalomethanes", value=60.0)
    turbidity = st.number_input("Turbidity", value=4.0)

# Prediction Button
if st.button("Predict Potability", use_container_width=True):
    # Collect features in numpy array
    features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    # Predict
    prediction = model.predict(features)
    
    # Display Result
    st.markdown("---")
    if prediction[0] == 1:
        st.success("✅ The water is **Potable** (Safe to Drink).")
    else:
        st.error("⚠️ The water is **Not Potable** (Unsafe to Drink).")