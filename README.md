# 🚀 Customer Churn Prediction App

End-to-end ML project predicting **telecom customer churn** using Logistic Regression (**F1 = 0.61**).

🔗 **Live Demo:** https://churn-prediction-app1.onrender.com  

[![Open Streamlit App](screenshots/low-risk.png)](https://churn-prediction-app1.onrender.com)

---

## 📊 Model Performance

| Model                | Accuracy | F1‑Score | Recall |
|----------------------|----------|----------|--------|
| Logistic Regression  | **80.1%** | **61.0%** | **58.6%** |
| Random Forest        | 78.6%    | 54.6%    | 48.4% |
| Decision Tree        | 76.8%    | 52.9%    | 49.2% |

---

## ✨ Key Features

- Uses **21 telecom features** such as tenure, contract type, monthly/total charges, and subscribed services.
- Full **scikit‑learn preprocessing pipeline** (encoding + scaling) wrapped with the model for safe deployment.
- **Streamlit web app** for instant churn risk predictions with a simple, business-friendly UI.
- Shows **churn probability** and a clear **risk label** (Low / High) for each customer.
- Includes space for **business recommendations** like discounts, retention calls, or cross‑sell offers.

---

## 📱 Screenshots

### Low‑Risk Customer  
![Low Risk](screenshots/low-risk.png)

### High‑Risk Customer  
![High Risk](screenshots/high-risk.png)

---

## 🛠️ Tech Stack

- **Language & Libraries:** Python, pandas, numpy, scikit‑learn, joblib, plotly  
- **ML:** Logistic Regression (plus Random Forest and Decision Tree baselines)  
- **App Framework:** Streamlit  
- **Deployment:** Render Web Service (Python 3.11, `pip install -r requirements.txt`)

---

## 🚀 Quick Start (Run Locally)

```bash
# Clone the repo
git clone https://github.com/VEERA16-16/churn-prediction-app.git
cd churn-prediction-app

# (Optional) create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
