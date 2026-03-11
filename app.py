import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("aqi_model.pkl")

st.title("Air Quality Index Prediction")

st.write("Enter pollutant levels to predict AQI")

city = st.number_input("City (Encoded Number)", min_value=0)
pm25 = st.number_input("PM2.5")
pm10 = st.number_input("PM10")
no2 = st.number_input("NO2")
so2 = st.number_input("SO2")
co = st.number_input("CO")
o3 = st.number_input("O3")
month = st.number_input("Month (1-12)", min_value=1, max_value=12)
day = st.number_input("Day of Week (0-6)")
year = st.number_input("Year")

if st.button("Predict AQI"):

    input_data = np.array([[city, pm25, pm10, no2, so2, co, o3, month, day, year]])

    prediction = model.predict(input_data)

    aqi = prediction[0]

    st.subheader(f"Predicted AQI: {aqi:.2f}")

    if aqi <= 50:
        st.success("Air Quality: Good")
    elif aqi <= 100:
        st.success("Air Quality: Satisfactory")
    elif aqi <= 200:
        st.warning("Air Quality: Moderate")
    elif aqi <= 300:
        st.warning("Air Quality: Poor")
    elif aqi <= 400:
        st.error("Air Quality: Very Poor")
    else:
        st.error("Air Quality: Severe")
