# 🏦 Telecom Customer Churn Prediction & Retention ML App

An end-to-end Machine Learning web application designed to forecast subscriber churn probability and recommend targeted retention strategies for telecom accounts. Powered by a Scikit-learn classification pipeline (ROC-AUC: **0.842**) and deployed via an interactive Streamlit web dashboard.

---

## 📌 Architecture & System Workflow

The pipeline ingests multi-attribute customer profiles, runs automated cleaning, encoding, and scaling transforms via a serialized pipeline (`churn_pipeline.joblib`), and outputs calibrated churn probabilities paired with retention actions.

```text
[ Raw Customer Input (Streamlit UI) ]
                  │
                  ▼
      [ Preprocessing Pipeline ]
  ├── Numeric Scaling (StandardScaler)
  └── Categorical Encoding (OneHotEncoder, handle_unknown="ignore")
                  │
                  ▼
      [ Logistic Regression Engine ]
       (ROC-AUC: 0.842 | C-regularized)
                  │
                  ▼
       [ Calibrated Risk Engine ]
  ├── Real-Time Risk Score (0.00 – 1.00)
  ├── Decision Boundary Thresholding (0.50)
  └── Action Matrix (Loyalty Discounts vs. Retention Incentives)

```

---

## 📊 Dataset Breakdown

Trained and evaluated on the **IBM Telco Customer Churn Dataset** (7,043 customer accounts across 21 feature attributes):

| Domain | Tracked Attributes |
| --- | --- |
| **Account Demographics** | Gender, Senior Citizen, Partner, Dependents |
| **Contract & Services** | Tenure (months), Contract Type, Internet Service, Tech Support, Streaming TV |
| **Billing & Payments** | Paperless Billing, Payment Method, Monthly Charges, Total Charges |
| **Target Variable** | `Churn` (1 = Customer Attrited, 0 = Customer Retained) |

---

## 📈 Model Performance & Evaluation

Evaluated against a stratified 20% holdout test set:

| Evaluation Metric | Test Score |
| --- | --- |
| **ROC-AUC** | **0.842** |
| **Precision (Churn = 1)** | **0.652** |
| **Recall (Churn = 1)** | **0.463** |
| **F1-Score** | **0.534** |

### Key Business & Feature Insights

1. **Tenure Impact:** Short customer tenure ($\le 12\text{ months}$) represents the single highest predictor of subscriber churn.
2. **Contract Duration:** Month-to-month contracts demonstrate a **$3\times$ higher churn rate** relative to one- or two-year commitments.
3. **High Monthly Spend + Fiber Optic:** Accounts with higher monthly billing tiers subscribed to Fiber Optic internet without attached Tech Support services demonstrate elevated attrition risk.

---

## 🚀 Interactive Streamlit Features

* **Dynamic Risk Simulation:** Sliders and dropdown menus for modifying customer contract types, payment methods, and spend variables.
* **Instant Risk Probability:** Real-time percentage calculation of attrition probability.
* **Prescriptive Action Plan:** Automated generation of recommended business decisions (e.g., contract upgrade incentives for high-risk accounts; upsell campaigns for low-risk accounts).
* **Interpretability Section:** Feature weight breakdowns explaining why a customer received their risk classification.

---

## 📂 Repository Structure

```text
telco-churn-prediction-streamlit/
├── data/                      # IBM Telco Churn CSV dataset
├── models/                    # Serialized model pipeline (churn_pipeline.joblib)
├── screenshots/               # UI application screenshots
├── src/                       # Source modules for training & evaluation
├── app.py                     # Streamlit frontend entrypoint
├── requirements.txt           # Locked dependencies
├── .gitignore                 # Exclusion rules for virtual environments and data
└── README.md                  # Project overview and reproduction instructions

```

---

## 🛠️ Tech Stack

* **Language:** Python 3.9+
* **ML Framework:** Scikit-learn, Joblib
* **Data Manipulation:** Pandas, NumPy
* **Application Framework:** Streamlit
* **Hosting:** Render

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/VEERA16-16/telco-churn-prediction-streamlit.git
cd telco-churn-prediction-streamlit

```

### 2. Set Up Virtual Environment

**Windows:**

```powershell
python -m venv .venv
.\.venv\Scripts\activate

```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the Application

```bash
streamlit run app.py

```

---

## 🌐 Live Deployment

Access the live interactive application on Render:

👉 **Live Web App:** [https://churn-prediction-app-5psk.onrender.com](https://churn-prediction-app-5psk.onrender.com)

---

## 👨‍💻 Author

**Veeramanikandan P**

*Aspiring Machine Learning & AI Engineer*

* GitHub: [@VEERA16-16](https://www.google.com/search?q=https://github.com/VEERA16-16)
* LinkedIn: [Veeramanikandan P](https://www.google.com/search?q=https://linkedin.com/in/mr-veeramanikandan-16v07p)
* Kaggle: [@veeramanikandan1](https://kaggle.com/veeramanikandan1)