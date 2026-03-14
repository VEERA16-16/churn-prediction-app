import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Churn Predictor", layout="wide")

@st.cache_resource
def load_model():
    model_path = "../models/logistic_regression_churn.joblib"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    st.error(f"❌ Model not found: {model_path}")
    st.stop()

model = load_model()
st.success("✅ Model loaded!")

st.title("🏦 **Customer Churn Predictor**")

# SIMPLIFIED inputs (only key features that matter most)
col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("📈 Tenure (months)", 0, 72, 12)
    contract = st.selectbox("📋 Contract", 
        ["Month-to-month", "One year", "Two year"])
    senior_citizen = st.selectbox("👴 Senior?", ["No", "Yes"])
    internet_service = st.selectbox("🌐 Internet", 
        ["DSL", "Fiber optic", "No"])
    monthly_charges = st.slider("💰 Monthly Charges ($)", 18, 120, 70)

with col2:
    total_charges = st.slider("💳 Total Charges ($)", 0, 9000, 2000)
    payment_method = st.selectbox("💳 Payment Method", 
        ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
    paperless_billing = st.selectbox("📄 Paperless?", ["No", "Yes"])
    device_protection = st.selectbox("🛡️ Device Protection?", ["No", "Yes"])
    tech_support = st.selectbox("🛠️ Tech Support?", ["No", "Yes"])
    streaming_tv = st.selectbox("📺 Streaming TV?", ["No", "Yes"])

if st.button("🔮 **Predict Churn**", type="primary", use_container_width=True):
    
    # Create FULL feature set (21 columns expected by model)
    input_data = {
        'gender': ['Male'],  # Fixed defaults for missing
        'SeniorCitizen': [senior_citizen],
        'Partner': ['No'],
        'Dependents': ['No'],
        'tenure': [tenure],
        'PhoneService': ['Yes'],
        'MultipleLines': ['No'],
        'InternetService': [internet_service],
        'OnlineSecurity': ['No'],
        'OnlineBackup': ['No'],
        'DeviceProtection': [device_protection],
        'TechSupport': [tech_support],
        'StreamingTV': [streaming_tv],
        'StreamingMovies': ['No'],
        'Contract': [contract],
        'PaperlessBilling': [paperless_billing],
        'PaymentMethod': [payment_method],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],
        'customerID': ['test_customer']  # Dummy ID
    }
    
    input_df = pd.DataFrame(input_data)
    
    # Predict
    churn_prob = model.predict_proba(input_df)[0, 1]
    
    col1.metric("Churn Risk", f"{churn_prob:.1%}")
    col2.metric("Status", "🚨 HIGH" if churn_prob > 0.5 else "✅ LOW")
    
    if churn_prob > 0.5:
        st.error("💡 **Retain:** Offer 20% discount")
    else:
        st.success("💰 **Upsell:** Premium services")
