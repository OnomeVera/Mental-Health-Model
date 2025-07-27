import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and scaler
model = joblib.load('mental_health_model.pkl')
scaler = joblib.load('scaler.pkl')

# List of features (must match training order)
features = ['Number', 'Sleep', 'Appetite', 'Interest', 'Fatigue',
            'Worthlessness', 'Agitation', 'Suicidal Ideation', 'Sleep Disturbance',
            'Aggression', 'Panic Attacks', 'Hopelessness', 'Restlessness', 'Low Energy']

st.title("🧠 Mental Health Concentration Predictor")

st.write("Please input the following symptom levels (e.g., 0 to 5) for prediction:")

# Collect user input
user_input = {}
for feature in features:
    user_input[feature] = st.number_input(f"{feature}:", min_value=0, max_value=10, value=0, step=1)

if st.button("Predict Concentration Level"):
    input_df = pd.DataFrame([user_input])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    st.success(f"🧠 Predicted Concentration Level: **{prediction[0]}**")