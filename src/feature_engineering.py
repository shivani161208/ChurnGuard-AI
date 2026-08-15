import numpy as np
import pandas as pd


def create_features(df):
    """
    Create all features used by the ChurnGuard-AI model.
    """

    df = df.copy()

    # -----------------------------
    # Tenure Group
    # -----------------------------
    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=[-1, 12, 24, 48, 72],
        labels=[
            "0-12 Months",
            "13-24 Months",
            "25-48 Months",
            "49-72 Months"
        ]
    )

    # -----------------------------
    # Average Monthly Spend
    # -----------------------------
    df["AvgMonthlySpend"] = np.where(
        df["tenure"] > 0,
        df["TotalCharges"] / df["tenure"],
        df["MonthlyCharges"]
    )

    # -----------------------------
    # Service Count
    # -----------------------------
    service_cols = [
        "PhoneService",
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    df["ServiceCount"] = 0

    for col in service_cols:
        df["ServiceCount"] += (
            df[col] == "Yes"
        ).astype(int)

    # -----------------------------
    # Security Support Count
    # -----------------------------
    support_cols = [
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport"
    ]

    df["SecuritySupportCount"] = 0

    for col in support_cols:
        df["SecuritySupportCount"] += (
            df[col] == "Yes"
        ).astype(int)

    # -----------------------------
    # New Customer
    # -----------------------------
    df["IsNewCustomer"] = (
        df["tenure"] <= 12
    ).astype(int)

    # -----------------------------
    # High Monthly Charge
    # -----------------------------
    df["HighMonthlyCharge"] = (
        df["MonthlyCharges"] > 70.35
    ).astype(int)

    # -----------------------------
    # Month-to-Month
    # -----------------------------
    df["IsMonthToMonth"] = (
        df["Contract"] == "Month-to-month"
    ).astype(int)

    # -----------------------------
    # Electronic Check
    # -----------------------------
    df["IsElectronicCheck"] = (
        df["PaymentMethod"] == "Electronic check"
    ).astype(int)

    # -----------------------------
    # High Risk Customer
    # -----------------------------
    df["HighRiskCustomer"] = (
        (df["IsNewCustomer"] == 1) &
        (df["IsMonthToMonth"] == 1)
    ).astype(int)

    return df