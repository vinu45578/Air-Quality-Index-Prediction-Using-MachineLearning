import streamlit as st
import joblib
import numpy as np

# Page config
st.set_page_config(
    page_title="AQI Prediction",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
}

h1 {
    color: #ffffff;
    text-align: center;
}

.card {
    background-color: #ffffff10;
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

div.stButton > button {
    background-color: #00c9ff;
    color: black;
    font-size: 18px;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)


# Load model
model = joblib.load("aqi_model.pkl")

# Title
st.title("🌫️ Air Quality Index Prediction Dashboard")

st.markdown("---")

# Input layout
col1, col2, col3 = st.columns(3)

with col1:
    pm25 = st.number_input("PM2.5", value=10.0)
    pm10 = st.number_input("PM10", value=10.0)
    no2 = st.number_input("NO2", value=5.0)

with col2:
    so2 = st.number_input("SO2", value=5.0)
    co = st.number_input("CO", value=1.0)
    o3 = st.number_input("O3", value=20.0)

with col3:
    city = st.number_input("City Encoded", value=1)
    month = st.number_input("Month", 1, 12)
    day = st.number_input("Day of Week (0-6)")
    year = st.number_input("Year", 2015, 2030)

st.markdown("---")

if st.button("🔍 Predict AQI"):

    input_data = np.array([[city, pm25, pm10, no2, so2, co, o3, month, day, year]])

    prediction = model.predict(input_data)

    aqi = prediction[0]

    st.subheader(f"Predicted AQI: {aqi:.2f}")

    if aqi <= 50:
        st.success("🟢 Good Air Quality")
    elif aqi <= 100:
        st.info("🟡 Satisfactory Air Quality")
    elif aqi <= 200:
        st.warning("🟠 Moderate Air Quality")
    elif aqi <= 300:
        st.warning("🔴 Poor Air Quality")
    elif aqi <= 400:
        st.error("🟣 Very Poor Air Quality")
    else:
        st.error("⚫ Severe Air Quality")
