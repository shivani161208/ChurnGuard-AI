import sys
import os

import streamlit as st
import plotly.graph_objects as go
import smtplib
from email.message import EmailMessage
from datetime import datetime
import pandas as pd
def send_feedback_email(feedback, feedback_text):

    sender = st.secrets["EMAIL_SENDER"]
    password = st.secrets["EMAIL_PASSWORD"]
    receiver = st.secrets["EMAIL_RECEIVER"]

    msg = EmailMessage()

    msg["Subject"] = "🛡️ ChurnGuard AI - New Feedback"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content(
        f"""
New feedback received from ChurnGuard AI.

Feedback: {feedback}

Comment:
{feedback_text}
"""
    )

    with smtplib.SMTP(
        "smtp.gmail.com",
        587
    ) as server:

        server.starttls()

        server.login(
            sender,
            password
        )

        server.send_message(msg)

def save_prediction_history(
    customer,
    result,
    risk_level
):

    history_dir = os.path.join(
        BASE_DIR,
        "data"
    )

    os.makedirs(
        history_dir,
        exist_ok=True
    )

    history_file = os.path.join(
        history_dir,
        "prediction_history.csv"
    )

    file_exists = os.path.exists(
        history_file
    )

    with open(
        history_file,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        import csv

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Timestamp",
                "Tenure",
                "Contract",
                "InternetService",
                "PaymentMethod",
                "MonthlyCharges",
                "TotalCharges",
                "ChurnProbability",
                "Prediction",
                "RiskLevel"
            ])

        prediction_status = (
            "Likely to Churn"
            if result["churn_prediction"] == 1
            else "Likely to Stay"
        )

        writer.writerow([
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            customer["tenure"],
            customer["Contract"],
            customer["InternetService"],
            customer["PaymentMethod"],
            customer["MonthlyCharges"],
            customer["TotalCharges"],
            result["churn_percentage"],
            prediction_status,
            risk_level
        ])


def admin_login():
    st.sidebar.header("🔐 Admin Panel")

    password = st.sidebar.text_input(
        "Admin Password",
        type="password"
    )

    return password == st.secrets["ADMIN_PASSWORD"]


st.set_page_config(
    page_title="ChurnGuard AI",
    page_icon="🛡️",
    layout="wide"
)
# ==========================================
# PATH SETUP
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

SRC_DIR = os.path.join(
    BASE_DIR,
    "src"
)

sys.path.append(SRC_DIR)

# ==========================================
# LOAD CSS
# ==========================================

CSS_PATH = os.path.join(
    BASE_DIR,
    "dashboard",
    "assets",
    "style.css"
)

with open(CSS_PATH) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# ==========================================
# IMPORTS
# ==========================================

from prediction import predict_churn
from recommendation import generate_recommendation



# ==========================================
# TITLE
# ==========================================

st.markdown(
    '<div class="main-title">🛡️ ChurnGuard AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Customer Churn Prediction & Retention System'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter customer information to estimate "
    "churn risk and receive retention recommendations."
)


# ==========================================
# CUSTOMER INFORMATION
# ==========================================

st.header("👤 Customer Information")

col1, col2, col3 = st.columns(3)


with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )


with col2:

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=72,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        [
            "No",
            "Yes",
            "No phone service"
        ]
    )

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )


with col3:

    online_security = st.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    online_backup = st.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    device_protection = st.selectbox(
        "Device Protection",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    tech_support = st.selectbox(
        "Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


# ==========================================
# SERVICES
# ==========================================

st.header("📺 Additional Services")

col1, col2, col3, col4 = st.columns(4)


with col1:

    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


with col2:

    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


with col3:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )


with col4:

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )


# ==========================================
# BILLING
# ==========================================

st.header("💳 Billing Information")

col1, col2 = st.columns(2)


with col1:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


with col2:

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=500.0
    )


# ==========================================
# CUSTOMER DICTIONARY
# ==========================================

customer = {

    "gender": gender,

    "SeniorCitizen": senior_citizen,

    "Partner": partner,

    "Dependents": dependents,

    "tenure": tenure,

    "PhoneService": phone_service,

    "MultipleLines": multiple_lines,

    "InternetService": internet_service,

    "OnlineSecurity": online_security,

    "OnlineBackup": online_backup,

    "DeviceProtection": device_protection,

    "TechSupport": tech_support,

    "StreamingTV": streaming_tv,

    "StreamingMovies": streaming_movies,

    "Contract": contract,

    "PaperlessBilling": paperless_billing,

    "PaymentMethod": payment_method,

    "MonthlyCharges": monthly_charges,

    "TotalCharges": total_charges
}


# ==========================================
# PREDICT BUTTON
# ==========================================

st.divider()

predict_button = st.button(
    "🔍 Predict Churn Risk",
    type="primary",
    use_container_width=True
)


# ==========================================
# PREDICTION
# ==========================================

if predict_button:

    try:

        result = predict_churn(customer)

        recommendation = generate_recommendation(
            customer,
            result["churn_probability"]
        )

        probability = result[
            "churn_percentage"
        ]

        risk_level = recommendation[
            "risk_level"
        ]
        save_prediction_history(
            customer,
            result,
            risk_level
        )
        st.success("✅ Prediction history saved successfully!")
        # ------------------------------
        # Results
        # ------------------------------

        # ==========================================
        # PREDICTION RESULT
        # ==========================================

        st.header("📊 Prediction Result")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Churn Probability",
                f"{probability:.2f}%"
            )

        with col2:

            st.metric(
                "Risk Level",
                risk_level
            )

        with col3:
            prediction = result["churn_prediction"]
            if prediction == 1:
                status = "Likely to Churn"
            else:
                status = "Likely to Stay"

            st.metric(
                "Prediction",
                status
            )


        # ==========================================
        # PROBABILITY GAUGE
        # ==========================================

        st.subheader("🎯 Churn Probability")

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=probability,
                number={
                    "suffix": "%"
                },
                title={
                    "text": "Churn Risk"
                },
                gauge={
                    "axis": {
                        "range": [0, 100]
                    },
                    "threshold": {
                        "line": {
                            "width": 4
                        },
                        "value": 50
                    }
                }
            )
        )

        fig.update_layout(
            height=350,
            margin={
                "l": 20,
                "r": 20,
                "t": 60,
                "b": 20
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

       

        # ==========================================
        # RISK ANALYSIS
        # ==========================================

        st.header("🧠 Risk Analysis")

        if result["churn_probability"] >= 0.70:

            st.error(
                "🔴 High Risk: This customer has a high "
                "probability of churn. Immediate retention "
                "action is recommended."
            )

        elif result["churn_probability"] >= 0.40:

            st.warning(
                "🟠 Medium Risk: This customer shows "
                "moderate churn risk. Proactive engagement "
                "is recommended."
            )

        else:

            st.success(
                "🟢 Low Risk: This customer has a relatively "
                "low probability of churn."
            )

        # ==========================================
        # RISK FACTORS
        # ==========================================

        st.header("🔎 Key Risk Factors")

        risk_factors = []

        if customer["Contract"] == "Month-to-month":
            risk_factors.append(
                "Month-to-month contract may increase churn risk."
            )

        if customer["tenure"] <= 12:
            risk_factors.append(
                "Customer is relatively new (12 months or less)."
            )

        if customer["PaymentMethod"] == "Electronic check":
            risk_factors.append(
                "Electronic check payment method may indicate higher churn risk."
            )

        if customer["MonthlyCharges"] > 70.35:
            risk_factors.append(
                "Monthly charges are relatively high."
            )

        if customer["TechSupport"] == "No":
            risk_factors.append(
                "Customer does not have technical support."
            )

        if customer["OnlineSecurity"] == "No":
            risk_factors.append(
                "Customer does not have online security."
            )

        if risk_factors:

            for factor in risk_factors:
                st.warning(f"⚠️ {factor}")

        else:

            st.success(
                "✅ No major customer risk factors detected."
            )
        # ==========================================
        # RETENTION RECOMMENDATIONS
        # ==========================================

        st.header("💡 Retention Recommendations")

        recommendations = recommendation[
            "recommendations"
        ]

        for i, rec in enumerate(
            recommendations,
            start=1
        ):

            st.info(
                f"**Action {i}:** {rec}"
            )


        # ==========================================
        # CUSTOMER PROFILE
        # ==========================================

        st.header("👤 Customer Risk Profile")

        profile_col1, profile_col2 = st.columns(2)

        with profile_col1:

            st.write(
                f"**Tenure:** {customer['tenure']} months"
            )

            st.write(
                f"**Contract:** {customer['Contract']}"
            )

            st.write(
                f"**Internet Service:** "
                f"{customer['InternetService']}"
            )

            st.write(
                f"**Payment Method:** "
                f"{customer['PaymentMethod']}"
            )


        with profile_col2:

            st.write(
                f"**Monthly Charges:** "
                f"₹{customer['MonthlyCharges']:.2f}"
            )

            st.write(
                f"**Total Charges:** "
                f"₹{customer['TotalCharges']:.2f}"
            )

            st.write(
                f"**Tech Support:** "
                f"{customer['TechSupport']}"
            )

            st.write(
                f"**Online Security:** "
                f"{customer['OnlineSecurity']}"
            )

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )

# ==========================================
# USER FEEDBACK
# ==========================================

st.header("💬 Feedback")

feedback = st.radio(
    "Was this prediction and recommendation helpful?",
    ["Yes", "No"],
    horizontal=True
)

feedback_text = st.text_area(
    "Additional Feedback (Optional)",
    placeholder="Tell us how we can improve..."
)

if st.button("📩 Submit Feedback"):

    try:

        # Save feedback locally
        import csv
        from datetime import datetime

        feedback_dir = os.path.join(
            BASE_DIR,
            "data"
        )

        os.makedirs(
            feedback_dir,
            exist_ok=True
        )

        feedback_file = os.path.join(
            feedback_dir,
            "feedback.csv"
        )

        file_exists = os.path.exists(
            feedback_file
        )

        with open(
            feedback_file,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "Timestamp",
                    "Feedback",
                    "Comment",
                    "ChurnProbability",
                    "RiskLevel"
                ])

            writer.writerow([
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                feedback,
                feedback_text,
                probability if "probability" in locals() else "",
                risk_level if "risk_level" in locals() else ""
            ])

        # Send email
        send_feedback_email(
            feedback,
            feedback_text
        )

        st.success(
            "✅ Thank you! Your feedback has been recorded and sent."
        )

    except Exception as e:

        st.error(
            f"❌ Feedback could not be sent: {e}"
        )

# ==========================================
# ADMIN FEEDBACK ANALYTICS
# ==========================================

if admin_login():

    st.success("🔓 Admin access granted")

    st.header("📊 Feedback Analytics")

    feedback_file = os.path.join(
        BASE_DIR,
        "data",
        "feedback.csv"
    )

    if os.path.exists(feedback_file):

        try:

            feedback_df = pd.read_csv(
                feedback_file
            )

            total_feedback = len(
                feedback_df
            )

            helpful_feedback = (
                feedback_df["Feedback"]
                .eq("Yes")
                .sum()
            )

            not_helpful_feedback = (
                feedback_df["Feedback"]
                .eq("No")
                .sum()
            )

            helpful_percentage = (
                helpful_feedback / total_feedback * 100
                if total_feedback > 0
                else 0
            )

            # KPI CARDS
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Total Feedback",
                    total_feedback
                )

            with col2:
                st.metric(
                    "👍 Helpful",
                    helpful_feedback
                )

            with col3:
                st.metric(
                    "👎 Not Helpful",
                    not_helpful_feedback
                )

            with col4:
                st.metric(
                    "Helpful Rate",
                    f"{helpful_percentage:.1f}%"
                )

            # CHART
            if total_feedback > 0:

                feedback_counts = (
                    feedback_df["Feedback"]
                    .value_counts()
                )

                fig = go.Figure(
                    data=[
                        go.Bar(
                            x=feedback_counts.index,
                            y=feedback_counts.values,
                            text=feedback_counts.values,
                            textposition="auto"
                        )
                    ]
                )

                fig.update_layout(
                    title="Feedback Distribution",
                    xaxis_title="Feedback",
                    yaxis_title="Number of Responses",
                    height=350
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            # RECENT FEEDBACK
            st.subheader("💬 Recent Feedback")

            display_columns = [
                "Timestamp",
                "Feedback",
                "Comment"
            ]

            available_columns = [
                col
                for col in display_columns
                if col in feedback_df.columns
            ]

            if available_columns:

                st.dataframe(
                    feedback_df[
                        available_columns
                    ].tail(10).iloc[::-1],
                    use_container_width=True
                )

        except Exception as e:

            st.error(
                f"Unable to load analytics: {e}"
            )

    else:

        st.info(
            "📭 No feedback has been submitted yet."
        )

    # ==========================================
    # PREDICTION HISTORY ANALYTICS
    # ==========================================

    st.header("📈 Prediction History")

    history_file = os.path.join(
        BASE_DIR,
        "data",
        "prediction_history.csv"
    )

    if os.path.exists(history_file):

        try:

            history_df = pd.read_csv(history_file)

            total_predictions = len(history_df)

            high_risk = (
                history_df["RiskLevel"]
                .eq("High Risk")
                .sum()
            )

            medium_risk = (
                history_df["RiskLevel"]
                .eq("Medium Risk")
                .sum()
            )

            low_risk = (
                history_df["RiskLevel"]
                .eq("Low Risk")
                .sum()
            )

            # ==========================================
            # KPI CARDS
            # ==========================================

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "🔍 Total Predictions",
                    total_predictions
                )

            with col2:
                st.metric(
                    "🔴 High Risk",
                    high_risk
                )

            with col3:
                st.metric(
                    "🟠 Medium Risk",
                    medium_risk
                )

            with col4:
                st.metric(
                    "🟢 Low Risk",
                    low_risk
                )

            # ==========================================
            # RISK DISTRIBUTION
            # ==========================================

            st.subheader("📊 Risk Distribution")

            risk_counts = (
                history_df["RiskLevel"]
                .value_counts()
            )

            fig = go.Figure(
                data=[
                    go.Bar(
                        x=risk_counts.index,
                        y=risk_counts.values,
                        text=risk_counts.values,
                        textposition="auto"
                    )
                ]
            )

            fig.update_layout(
                title="Customer Risk Distribution",
                xaxis_title="Risk Level",
                yaxis_title="Number of Customers",
                height=350
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # ==========================================
            # RECENT PREDICTIONS
            # ==========================================

            st.subheader("🕒 Recent Predictions")

            st.dataframe(
                history_df
                .tail(10)
                .iloc[::-1],
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"Unable to load prediction history: {e}"
            )

    else:

        st.info(
            "📭 No prediction history available yet."
        )
# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div class="footer">
        🛡️ ChurnGuard AI | Customer Churn Prediction &
        Retention System
    </div>
    """,
    unsafe_allow_html=True
)