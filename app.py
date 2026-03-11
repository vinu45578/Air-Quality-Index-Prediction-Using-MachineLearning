import streamlit as st
import joblib
import numpy as np

# Page configuration
st.set_page_config(
    page_title="AQI Prediction",
    page_icon="🌫️",
    layout="wide"
)

# Load model
model = joblib.load("aqi_model.pkl")

# Title
st.title("🌍 Air Quality Index Prediction")
st.markdown("Predict AQI using pollutant levels")

st.divider()

# Create 3 columns layout
col1, col2, col3 = st.columns(3)

with col1:
    city = st.number_input("City (Encoded)")
    pm25 = st.number_input("PM2.5")
    pm10 = st.number_input("PM10")

with col2:
    no2 = st.number_input("NO2")
    so2 = st.number_input("SO2")
    co = st.number_input("CO")

with col3:
    o3 = st.number_input("O3")
    month = st.number_input("Month", 1, 12)
    day = st.number_input("Day (0-6)")
    year = st.number_input("Year", 2015, 2030)

st.divider()

if st.button("🔍 Predict AQI"):

    input_data = np.array([[city, pm25, pm10, no2, so2, co, o3, month, day, year]])

    prediction = model.predict(input_data)

    aqi = prediction[0]

    st.subheader(f"Predicted AQI: {aqi:.2f}")

    if aqi <= 50:
        st.success("Good Air Quality 😊")
    elif aqi <= 100:
        st.info("Satisfactory Air Quality")
    elif aqi <= 200:
        st.warning("Moderate Air Quality")
    elif aqi <= 300:
        st.warning("Poor Air Quality")
    elif aqi <= 400:
        st.error("Very Poor Air Quality")
    else:
        st.error("Severe Air Quality ⚠️")
