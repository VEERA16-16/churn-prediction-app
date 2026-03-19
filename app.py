import streamlit as st
import os
import joblib
import pandas as pd
import numpy as np

st.set_page_config(page_title="Churn Predictor", layout="wide")

# ---- Load model once, from correct path ----
@st.cache_resource
def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "models", "logistic_regression_churn.joblib")
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
    contract = st.selectbox(
        "📋 Contract",
        ["Month-to-month", "One year", "Two year"]
    )
    senior_citizen = st.selectbox("👴 Senior?", ["No", "Yes"])
    internet_service = st.selectbox(
        "🌐 Internet",
        ["DSL", "Fiber optic", "No"]
    )
    monthly_charges = st.slider("💰 Monthly Charges ($)", 18, 120, 70)

with col2:
    total_charges = st.slider("💳 Total Charges ($)", 0, 9000, 2000)
    payment_method = st.selectbox(
        "💳 Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
    )
    paperless_billing = st.selectbox("📄 Paperless?", ["No", "Yes"])
    device_protection = st.selectbox("🛡️ Device Protection?", ["No", "Yes"])
    tech_support = st.selectbox("🛠️ Tech Support?", ["No", "Yes"])
    streaming_tv = st.selectbox("📺 Streaming TV?", ["No", "Yes"])

if st.button("🔮 **Predict Churn**", type="primary", use_container_width=True):

    # Map Yes/No to numeric flags where the model expects numbers
    senior_citizen_num = 1 if senior_citizen == "Yes" else 0
    paperless_billing_flag = 1 if paperless_billing == "Yes" else 0
    device_protection_flag = 1 if device_protection == "Yes" else 0
    tech_support_flag = 1 if tech_support == "Yes" else 0
    streaming_tv_flag = 1 if streaming_tv == "Yes" else 0


    # Build input row with correct dtypes

input_data = {
    "gender": gender,  # string, e.g. "Male" / "Female"
    "SeniorCitizen": int(senior_citizen_num),  # numeric 0/1
    "Partner": "No",  # or from UI if you later add it
    "Dependents": "No",
    "tenure": float(tenure),  # numeric
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": internet_service,  # e.g. "DSL", "Fiber optic", "No"
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "Yes" if device_protection_flag else "No",
    "TechSupport": "Yes" if tech_support_flag else "No",
    "StreamingTV": "Yes" if streaming_tv_flag else "No",
    "StreamingMovies": "No",
    "Contract": contract,  # e.g. "Month-to-month"
    "PaperlessBilling": "Yes" if paperless_billing_flag else "No",
    "PaymentMethod": payment_method,  # e.g. "Electronic check"
    "MonthlyCharges": float(monthly_charges),
    "TotalCharges": float(total_charges) if total_charges not in ["", None] else 0.0,
    "customerID": "test_customer",
}

input_df = pd.DataFrame([input_data])


    # Predict
churn_prob = model.predict_proba(input_df)[0, 1]

col1.metric("Churn Risk", f"{churn_prob:.1%}")
col2.metric("Status", "🚨 HIGH" if churn_prob > 0.5 else "✅ LOW")

st.success(f"**Churn Risk: {churn_status}**")
st.info(f"**Probability: {churn_prob:.1%}**")
st.progress(churn_prob)
st.caption("Model predicts the chance this customer will leave in the next period.")


if churn_prob > 0.5:
        st.error("💡 **Retain:** Offer 20% discount")
else:
        st.success("💰 **Upsell:** Premium services")
