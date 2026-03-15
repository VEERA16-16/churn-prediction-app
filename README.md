# 🚀 Customer Churn Prediction App

End‑to‑end ML project predicting **telecom customer churn** using Logistic Regression (**F1 = 0.61**). [file:2]

[![Open Streamlit App](screenshots/low-risk.png)](https://YOUR-RENDER-URL.onrender.com)

---

## 📊 Model Performance

| Model                | Accuracy | F1‑Score | Recall |
|----------------------|----------|----------|--------|
| Logistic Regression  | **80.1%** | **61.0%** | **58.6%** |
| Random Forest       | 78.6%    | 54.6%    | 48.4% |
| Decision Tree       | 76.8%    | 52.9%    | 49.2% |

---

## ✨ Key Features

- Uses **21 customer features** (tenure, contract type, charges, services). [file:2]  
- Full **preprocessing pipeline** with One‑Hot encoding and scaling. [file:2]  
- **Streamlit web app** for instant churn risk predictions.  
- Separate views for **low‑risk** and **high‑risk** customers.  
- Business‑friendly outputs: churn probability + risk label. [file:2]

---

## 📱 Screenshots

### Low‑Risk Customer  
![Low Risk](screenshots/low-risk.png)

### High‑Risk Customer  
![High Risk](Screenshot 2026-03-14 222037.png)

---

## 🛠️ Tech Stack

- Python, pandas, numpy, scikit‑learn, joblib.  
- Streamlit for the UI.  
- Deployed on **Render** (Web Service). [web:40]

---

## 🚀 Quick Start (Local)

```bash
# Clone
git clone https://github.com/VEERA16-16/churn-prediction-app.git
cd churn-prediction-app

# (Optional) virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
