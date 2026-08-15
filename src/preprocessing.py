import pandas as pd
import joblib


def clean_data(df):
    """
    Basic data cleaning for churn dataset.
    """

    df = df.copy()

    # Remove customer ID
    df = df.drop(
        columns=["customerID"],
        errors="ignore"
    )

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Fill missing TotalCharges
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    return df


def encode_target(df):
    """
    Convert Churn Yes/No into 1/0.
    """

    df = df.copy()

    if "Churn" in df.columns:

        df["Churn"] = df["Churn"].map({
            "No": 0,
            "Yes": 1
        })

    return df


def preprocess_for_model(
    df,
    preprocessor
):
    """
    Apply already-fitted sklearn preprocessor.
    """

    df = df.copy()

    X_processed = preprocessor.transform(df)

    return X_processed


def load_preprocessor(path):
    """
    Load saved preprocessing pipeline.
    """

    return joblib.load(path)