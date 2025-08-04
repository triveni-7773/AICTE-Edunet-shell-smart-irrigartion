import streamlit as st
import numpy as np
import joblib


model = joblib.load("Farm_Irrigation_System.pkl")


st.set_page_config(page_title="Smart Sprinkler System", page_icon="🚿", layout="centered")


st.markdown("""
    <style>
        .main {
            background-color: #f0f8ff;
        }

        /* Predict Sprinklers button default style */
        div.stButton > button {
            background-color: #0A84FF;  /* Default blue */
            color: white !important;    /* White text */
            padding: 0.6em 1.2em;
            border-radius: 8px;
            font-size: 18px;
            transition: background-color 0.3s ease;
            border: none;
        }

        /* Hover effect with light blue and white text */
        div.stButton > button:hover {
            background-color: #66B2FF;  /* Light blue */
            color: white !important;    /* Ensure white text stays */
        }

        .stSlider > div {
            padding-top: 0.3rem;
        }
    </style>
""", unsafe_allow_html=True)


st.title("🚿 Smart Sprinkler System")
st.markdown("### 🌿 Enter Scaled Sensor Values (0 to 1) to Predict Sprinkler Status")
st.markdown("Use the sliders below to simulate sensor readings and check whether each sprinkler should be **ON** or **OFF**.")


sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)


if st.button("🔍 Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### 🔧 Sprinkler Prediction Results")
    for i, status in enumerate(prediction):
        if status == 1:
            st.success(f"✅ Sprinkler {i} (parcel_{i}) is **ON**")
        else:
            st.error(f"❌ Sprinkler {i} (parcel_{i}) is **OFF**")
