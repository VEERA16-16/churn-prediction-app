import streamlit as st
import os
import joblib
import pandas as pd

st.set_page_config(page_title="Churn Predictor", layout="wide")

# ===== LOAD PIPELINE MODEL =====
@st.cache_resource
def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "models", "churn_pipeline.joblib")

    if os.path.exists(model_path):
        return joblib.load(model_path)

    st.error(f"❌ Model not found: {model_path}")
    st.stop()

model = load_model()
st.success("✅ Model loaded successfully!")

# ===== TITLE =====
st.title("🏦 Customer Churn Predictor")

# ===== INPUT UI =====
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    tenure = st.slider("📈 Tenure (months)", 0, 72, 12)

    contract = st.selectbox(
        "📋 Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    senior_citizen = st.selectbox("👴 Senior Citizen?", ["No", "Yes"])

    internet_service = st.selectbox(
        "🌐 Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    monthly_charges = st.slider("💰 Monthly Charges ($)", 18, 120, 70)

with col2:
    total_charges = st.slider("💳 Total Charges ($)", 0, 9000, 2000)

    payment_method = st.selectbox(
        "💳 Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)",
        ]
    )

    paperless_billing = st.selectbox("📄 Paperless Billing?", ["No", "Yes"])
    device_protection = st.selectbox("🛡️ Device Protection?", ["No", "Yes"])
    tech_support = st.selectbox("🛠️ Tech Support?", ["No", "Yes"])
    streaming_tv = st.selectbox("📺 Streaming TV?", ["No", "Yes"])

# ===== PREDICTION BUTTON =====
if st.button("🔮 Predict Churn", type="primary", use_container_width=True):

    try:
        # ===== BUILD INPUT DATA =====
        input_data = {
            "customerID": "test_customer",
            "gender": gender,
            "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
            "Partner": "No",
            "Dependents": "No",
            "tenure": float(tenure),
            "PhoneService": "Yes",
            "MultipleLines": "No",
            "InternetService": internet_service,
            "OnlineSecurity": "No",
            "OnlineBackup": "No",
            "DeviceProtection": device_protection,
            "TechSupport": tech_support,
            "StreamingTV": streaming_tv,
            "StreamingMovies": "No",
            "Contract": contract,
            "PaperlessBilling": paperless_billing,
            "PaymentMethod": payment_method,
            "MonthlyCharges": float(monthly_charges),
            "TotalCharges": float(total_charges),
        }

        input_df = pd.DataFrame([input_data])
       

        # ===== PREDICTION =====
        churn_prob = model.predict_proba(input_df)[0, 1]

        # ===== RISK LEVEL =====
        risk_label = "🚨 HIGH RISK" if churn_prob > 0.5 else "✅ LOW RISK"

        st.subheader("📊 Prediction Result")

        col1, col2 = st.columns(2)
        col1.metric("Churn Probability", f"{churn_prob:.2%}")
        col2.metric("Risk Level", risk_label)

        # Progress bar
        st.progress(float(churn_prob))

        # ===== BUSINESS INSIGHT =====
        if churn_prob > 0.5:
            st.error("💡 Suggestion: Offer discount or retention plan")
        else:
            st.success("💰 Suggestion: Upsell premium services")

    except Exception as e:
        st.error(f"❌ Prediction Error: {e}")

with st.expander("ℹ️ Model Info"):
    st.markdown("""
**Dataset**

- IBM Telco Customer Churn dataset (7,043 customers, 19 features + churn label).
- Target variable: `Churn` (1 = customer left, 0 = stayed).

**Model**

- Algorithm: Logistic Regression (with class labels 0/1).
- Preprocessing:
  - Numeric features (`tenure`, `MonthlyCharges`, `TotalCharges`) are standardized.
  - Categorical features (e.g., `Contract`, `InternetService`, `PaymentMethod`) are one‑hot encoded with `handle_unknown="ignore"`.

**Evaluation (on 20% test set)**

- ROC‑AUC: **0.842**
- Recall (Churn=1, threshold 0.50): **0.463**

**Interpretation**

- Higher churn probability → customer is more likely to leave.
- Threshold 0.50 is used to label **High Risk** vs **Low Risk** in this app.
- In analysis, shorter tenure, month‑to‑month contracts, and higher monthly charges were the strongest churn drivers.
""")
st.markdown("---")
st.caption("Built as a portfolio project: Telecom Customer Churn Prediction (Logistic Regression pipeline).")
