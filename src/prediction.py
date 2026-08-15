import os
import joblib
import pandas as pd

from feature_engineering import create_features
from preprocessing import clean_data


# ==========================================
# PATHS
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "churn_model.pkl"
)

PREPROCESSOR_PATH = os.path.join(
    BASE_DIR,
    "models",
    "preprocessor.pkl"
)


# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load(
    MODEL_PATH
)

preprocessor = joblib.load(
    PREPROCESSOR_PATH
)


# ==========================================
# PREDICTION
# ==========================================

def predict_churn(customer_data):

    df = pd.DataFrame(
        [customer_data]
    )

    # Cleaning
    df = clean_data(df)

    # Feature engineering
    df = create_features(df)

    # Match training columns
    expected_columns = (
        preprocessor.feature_names_in_
    )

    missing_columns = (
        set(expected_columns)
        - set(df.columns)
    )

    if missing_columns:

        raise ValueError(
            f"Missing input columns: "
            f"{missing_columns}"
        )

    df = df[
        expected_columns
    ]

    # Preprocessing
    X_processed = (
        preprocessor.transform(df)
    )

    # Prediction probability
    probability = (
        model.predict_proba(
            X_processed
        )[0][1]
    )

    prediction = int(
        probability >= 0.5
    )

    return {
        "churn_prediction": prediction,

        "churn_probability": round(
            float(probability),
            4
        ),

        "churn_percentage": round(
            float(probability * 100),
            2
        )
    }