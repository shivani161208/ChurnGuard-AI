# 🛡️ ChurnGuard AI

## Customer Churn Prediction & Retention System

ChurnGuard AI is an end-to-end Machine Learning application designed to predict customer churn and help businesses take proactive retention actions.

The system analyzes customer information, predicts the probability of churn, identifies important risk factors, and provides personalized retention recommendations through an interactive Streamlit dashboard.

---

## 🎯 Project Objective

Customer churn is an important challenge for subscription-based businesses.

ChurnGuard AI helps businesses:

- 🔮 Predict whether a customer is likely to churn
- 📊 Calculate the customer's churn probability
- 🚦 Classify customers into Low, Medium, and High Risk
- 🔎 Identify important churn risk factors
- 💡 Generate personalized retention recommendations
- 📈 Track prediction history
- 💬 Collect user feedback
- 📧 Send feedback notifications through email
- 🔐 Provide an admin analytics dashboard

---

## 🚀 Key Features

### 🔮 Customer Churn Prediction

Predicts whether a customer is:

- 🟢 Likely to Stay
- 🔴 Likely to Churn

### 📊 Churn Probability

Provides a numerical churn probability between 0% and 100%.

Example:

    Churn Probability: 78.42%
    Prediction: Likely to Churn
    Risk Level: High Risk

### 🚦 Risk Classification

Customers are classified into:

- 🟢 Low Risk
- 🟠 Medium Risk
- 🔴 High Risk

### 🔎 Risk Factor Analysis

The system analyzes important customer attributes such as:

- Contract type
- Customer tenure
- Payment method
- Monthly charges
- Technical support
- Online security
- Internet service

### 💡 Retention Recommendations

ChurnGuard AI generates personalized retention strategies based on customer information and churn probability.

Possible actions include:

- Offer a contract upgrade
- Provide technical support
- Offer a personalized discount
- Improve customer engagement
- Encourage long-term plans

### 📈 Prediction History

The application stores prediction history including:

- Timestamp
- Customer tenure
- Contract
- Internet service
- Payment method
- Monthly charges
- Total charges
- Churn probability
- Prediction
- Risk level

### 💬 Feedback System

Users can provide feedback about the prediction and recommendations.

The feedback system stores:

- Feedback response
- Additional comments
- Churn probability
- Risk level
- Timestamp

### 📧 Email Notification

The application can send feedback notifications through Gmail SMTP.

Sensitive credentials are stored using Streamlit Secrets and are excluded from GitHub.

### 🔐 Admin Dashboard

The admin section provides:

- Total feedback
- Helpful feedback
- Not helpful feedback
- Helpful feedback percentage
- Feedback distribution
- Recent feedback
- Total predictions
- High-risk customers
- Medium-risk customers
- Low-risk customers
- Recent predictions
- Risk distribution

### 📊 Interactive Dashboard

The Streamlit dashboard provides:

- Churn probability gauge
- Risk analysis
- Risk factor analysis
- Retention recommendations
- Customer profile
- Feedback analytics
- Prediction history analytics
- Risk distribution charts

---

# 🧠 Machine Learning

ChurnGuard AI uses multiple Machine Learning algorithms for customer churn prediction.

### Logistic Regression

Used as an interpretable baseline classification model.

### Random Forest

An ensemble learning algorithm used to capture nonlinear relationships and understand feature importance.

### XGBoost

A powerful gradient boosting algorithm used for high-performance classification.

---

## 🔄 Machine Learning Workflow

    Raw Customer Data
            ↓
    Data Cleaning
            ↓
    Exploratory Data Analysis
            ↓
    Feature Engineering
            ↓
    Data Preprocessing
            ↓
    Train/Test Split
            ↓
    Model Training
            ↓
    Model Evaluation
            ↓
    Best Model Selection
            ↓
    Model Serialization
            ↓
    Streamlit Prediction

Trained models and preprocessing objects are saved using Joblib so that predictions can be generated without retraining the models every time.

---

# 🛠️ Tech Stack

### Programming

- Python

### Machine Learning

- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib

### Data Analysis

- Jupyter Notebook
- Exploratory Data Analysis
- Feature Engineering

### Visualization

- Streamlit
- Plotly

### Database

- MySQL
- SQLite

### Development Tools

- VS Code
- Git
- GitHub
- Jupyter Notebook

---

# 📂 Project Structure

    ChurnGuard-AI/
    │
    ├── data/
    │   ├── raw/
    │   │   └── customer_churn.csv
    │   │
    │   └── processed/
    │       ├── churn.db
    │       ├── churn_feature_engineered.csv
    │       ├── pchurn_train_processed.csv
    │       └── pchurn_test_processed.csv
    │
    ├── models/
    │   ├── churn_model.pkl
    │   ├── feature_columns.pkl
    │   ├── logistic_model.pkl
    │   ├── preprocessor.pkl
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

---

# ⚡ Quick Start

## 1. Clone the Repository

    git clone https://github.com/shivani161208/ChurnGuard-AI.git

    cd ChurnGuard-AI

## 2. Create Virtual Environment

    python -m venv venv

### Windows

    venv\Scripts\activate

## 3. Install Dependencies

    pip install -r requirements.txt

## 4. Configure Streamlit Secrets

Create:

    dashboard/.streamlit/secrets.toml

Add your own credentials:

    EMAIL_SENDER = "your_email@gmail.com"
    EMAIL_PASSWORD = "your_app_password"
    EMAIL_RECEIVER = "your_email@gmail.com"
    ADMIN_PASSWORD = "your_admin_password"

Never upload `secrets.toml` to GitHub.

## 5. Run the Application

    streamlit run dashboard/app.py

The application will open at:

    http://localhost:8501

---

# 📊 Dashboard Workflow

    Customer Information
            ↓
    Predict Churn Risk
            ↓
    Churn Probability
            ↓
    Risk Classification
            ↓
    Risk Factor Analysis
            ↓
    Retention Recommendations
            ↓
    Prediction History
            ↓
    User Feedback
            ↓
    Admin Analytics

---

# 🔐 Security

ChurnGuard AI follows basic security practices for sensitive credentials.

- Admin authentication
- Streamlit Secrets for credentials
- `.gitignore` for sensitive files
- Credentials are not stored directly in Python source code
- Sensitive configuration files are excluded from GitHub

Important sensitive file:

    dashboard/.streamlit/secrets.toml

This file should never be committed to GitHub.

---

# 📌 Future Improvements

- [ ] Streamlit Cloud deployment
- [ ] SHAP-based model explainability
- [ ] Customer segmentation
- [ ] Real-time database integration
- [ ] Downloadable prediction reports
- [ ] Retention ROI estimation
- [ ] Multiple admin roles
- [ ] Automated model retraining
- [ ] Cloud database integration
- [ ] Advanced customer analytics
- [ ] Real-time churn monitoring

---

# 🎓 Learning Outcomes

This project demonstrates practical knowledge of:

- Machine Learning
- Classification
- Data preprocessing
- Feature engineering
- Model evaluation
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SQL
- MySQL
- SQLite
- Streamlit
- Plotly
- Git
- GitHub
- Email automation
- Dashboard development

---

# 👩‍💻 Author

## Shivani

B.Tech Computer Science & Engineering

KIPM College of Engineering & Technology

---

# 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you find this project useful, please consider giving the repository a star on GitHub.

Thank you for visiting ChurnGuard AI! 🛡️
