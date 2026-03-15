# 🚀 Customer Churn Prediction App

**End-to-end ML project** predicting telecom customer churn using Logistic Regression (**F1 = 0.61**). [file:2]

[![Streamlit App](screenshots/low-risk.png)](https://YOUR-RENDER-URL.onrender.com)

## 📊 Model Performance
| Model              | Accuracy | F1-Score | Recall |
|--------------------|----------|----------|--------|
| Logistic Regression | **80.1%** | **61.0%** | **58.6%** |
| Random Forest       | 78.6%    | 54.6%    | 48.4% |
| Decision Tree       | 76.8%    | 52.9%    | 49.2% |

## ✨ Features
- **21 telecom features** (tenure, contract, charges, services). [file:2]
- **Preprocessing pipeline** (OneHot encoding + scaling) wrapped in scikit‑learn `Pipeline`. [file:2]
- **Streamlit web app** for instant churn predictions.
- **Business recommendations** based on high‑risk customer segments. [file:2]

## 📱 Live Demo
### Low Risk Customer
![Low Risk](screenshots/low-risk.png)

### High Risk Customer  
![High Risk](screenshots/high-risk.png)

## 🛠️ Tech Stack
- Python, pandas, numpy, scikit‑learn, joblib.
- Streamlit for the web UI.
- Render for deployment (Web Service with `Procfile` + `requirements.txt`). [web:40]

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/VEERA16-16/churn-prediction-app.git
cd churn-prediction-app

# (Optional) create virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install
pip install -r requirements.txt

# Run app
streamlit run app.py

      
