# 🛡️ ChurnGuard AI

### Customer Churn Prediction & Retention System

ChurnGuard AI is an end-to-end Machine Learning application that predicts
customer churn probability and provides personalized retention
recommendations.

---

## 🚀 Features

- 🔮 Customer churn prediction
- 📊 Churn probability estimation
- 🚦 Low, Medium and High risk classification
- 🔎 Key churn risk factor analysis
- 💡 Personalized retention recommendations
- 📈 Prediction history analytics
- 💬 User feedback collection
- 📧 Email notification for feedback
- 🔐 Admin dashboard
- 📊 Interactive Plotly visualizations
- 🎨 Streamlit dashboard

---

## 🧠 Machine Learning

The project uses multiple machine learning models for customer churn
prediction:

- Logistic Regression
- Random Forest
- XGBoost

The trained model and preprocessing components are saved using Joblib
for faster prediction without retraining the model.

---

## 🛠️ Tech Stack

### Programming
- Python

### Machine Learning
- Pandas
- NumPy
- Scikit-learn
- XGBoost

### Visualization
- Plotly
- Streamlit

### Database
- MySQL
- SQLite

### Development Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## 📂 Project Structure

```text
ChurnGuard-AI/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── churn_model.pkl
│   ├── feature_columns.pkl
│   ├── preprocessor.pkl
│   ├── logistic_model.pkl
│   ├── random_forest_model.pkl
│   └── xgboost_model.pkl
│
├── notebook/
│   ├── 1_EDA.ipynb
│   ├── 2_data_preprocessing.ipynb
│   ├── 3_feature_engineering.ipynb
│   ├── 4_sql_analysis.ipynb
│   ├── 5_model_training.ipynb
│   └── 6_model_evalution.ipynb
│
├── sql/
│   ├── churn_analysis.sql
│   └── customer_analysis.sql
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── prediction.py
│   ├── recommendation.py
│   └── load_to_mysql.py
│
├── dashboard/
│   ├── app.py
│   └── assets/
│       └── style.css
│
├── requirements.txt
├── .gitignore
└── README.md
