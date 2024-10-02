import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd

# Load the Random Forest model
filename = 'rf_model.sav'
with open(filename, 'rb') as file:
    rf_classifier = pickle.load(file)

# Function to make predictions
def predict_stroke(features):
    return rf_classifier.predict([features])

# Main function to show the Stroke Prediction App
def show_main_page():
    # Sidebar navigation
    with st.sidebar:
        selected = option_menu("Stroke Prediction App", ["Home", "Predict"], 
                               icons=["house", "stethoscope"], 
                               menu_icon="cast", default_index=0)

    # Home page
    if selected == "Home":
        st.title("Stroke Prediction App")
        st.write("### Welcome to the Stroke Prediction Model")
        st.write("""
        This application predicts the risk of stroke based on various health parameters.
        Stroke is a medical emergency that occurs when blood flow to the brain is interrupted. 
        It's important to understand the risk factors that contribute to stroke in order to take preventive measures.
        """)
        st.image("https://www.healthywomen.org/media-library/stroke-vs-heart-attack-know-the-signs-symptoms.png?id=32931472&width=1200&height=800&quality=85&coordinates=0%2C0%2C0%2C1")  # Replace with the path to your image
        st.write("""
        Please navigate to the 'Predict' tab to use the stroke prediction model.
        """)

    # Prediction page
    if selected == "Predict":
        st.title("Stroke Prediction")
        st.write("Enter the following details to predict the likelihood of a stroke.")

        # Input fields
        age = st.number_input("Age", min_value=0, max_value=120)
        hypertension = st.selectbox("Hypertension", options=["No", "Yes"])
        heart_disease = st.selectbox("Heart Disease", options=["No", "Yes"])
        avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0)
        bmi = st.number_input("BMI", min_value=0.0)
        gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
        ever_married = st.selectbox("Ever Married", options=["Yes", "No"])
        work_type = st.selectbox("Work Type", options=["Never worked","Gov-Job", "Private", "Self-employed", "Children"])
        residence_type = st.selectbox("Residence Type", options=["Urban", "Rural"])
        smoking_status = st.selectbox("Smoking Status", options=["formerly smoked", "never smoked", "smokes","unknown"])

        # One-hot encoding of categorical features
        hypertension = 1 if hypertension == "Yes" else 0
        heart_disease = 1 if heart_disease == "Yes" else 0
        gender_Male = 1 if gender == "Male" else 0
        gender_Other = 1 if gender == "Other" else 0
        ever_married_Yes = 1 if ever_married == "Yes" else 0
        work_type_Never_worked = 1 if work_type == "Never worked" else 0
        work_type_Private = 1 if work_type == "Private" else 0
        work_type_Self_employed = 1 if work_type == "Self-employed" else 0
        work_type_children = 1 if work_type == "Children" else 0
        Residence_type_Urban = 1 if residence_type == "Urban" else 0
        smoking_status_formerly = 1 if smoking_status == "formerly smoked" else 0
        smoking_status_never = 1 if smoking_status == "never smoked" else 0
        smoking_status_smokes = 1 if smoking_status == "smokes" else 0

        # Prepare features for prediction
        features = [
            age,
            hypertension,
            heart_disease,
            avg_glucose_level,
            bmi,
            gender_Male,
            gender_Other,
            ever_married_Yes,
            work_type_Never_worked,
            work_type_Private,
            work_type_Self_employed,
            work_type_children,
            Residence_type_Urban,
            smoking_status_formerly,
            smoking_status_never,
            smoking_status_smokes
        ]

        # Predict button
        if st.button("Predict Stroke Risk"):
            prediction = predict_stroke(features)
            if prediction[0] == 1:
                st.error("The model predicts that there is a high risk of stroke.")
            else:
                st.success("The model predicts that there is a low risk of stroke.")

# Run the app using: streamlit run loading.py
