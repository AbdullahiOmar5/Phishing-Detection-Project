# serve_utils.py
import json
import joblib
import pandas as pd
import numpy as np
import os

# ===========================
# 🔧 Load Pre-Fitted Objects
# ===========================
SCALER_PATH = "../models/scaler_top20.pkl"  # Ensure you saved the top20 scaler with this name
TOP_FEATURES_PATH = "../models/top20_features.json"

# Load scaler
SCALER = joblib.load(SCALER_PATH)

# Load features used for training
if os.path.exists(TOP_FEATURES_PATH):
    TRAIN_COLUMNS = json.load(open(TOP_FEATURES_PATH))
else:
    raise FileNotFoundError("Missing top20_features.json in models folder.")

# Load trained models (top 20-feature models)
MODEL_PATHS = {
    "logistic_regression": "../models/Logistic_Regression_top20.pkl",
    "random_forest": "../models/Random_Forest_top20.pkl",
    "decision_tree": "../models/Decision_Tree_top20.pkl"
}

MODELS = {}
for name, path in MODEL_PATHS.items():
    if os.path.exists(path):
        MODELS[name] = joblib.load(path)
    else:
        print(f"⚠️ Warning: Model file not found for {name} at {path}")


# ===========================
# 🧩 Feature Preparation
# ===========================
def prepare_features_from_raw(record: dict) -> pd.DataFrame:
    """
    Prepare a single record for phishing prediction.
    Ensures:
      - Columns match the scaler's training features (top20)
      - Missing columns are filled with zeros
      - Extra columns are ignored
    """
    scaler_features = list(SCALER.feature_names_in_) if hasattr(SCALER, "feature_names_in_") else TRAIN_COLUMNS

    # Initialize with zeros for all expected features
    row = {col: 0.0 for col in scaler_features}

    # Fill available values from the record
    for name, val in record.items():
        if name in row:
            try:
                row[name] = float(val)
            except:
                row[name] = 0.0  # Handle non-numeric gracefully

    # Create DataFrame with the correct order
    df_one = pd.DataFrame([row], columns=scaler_features)

    # Transform safely
    df_scaled = pd.DataFrame(SCALER.transform(df_one), columns=scaler_features)

    return df_scaled


# ===========================
# 🔮 Prediction Function
# ===========================
def predict_phishing(record: dict, model_name: str = "random_forest") -> dict:
    """
    Predict phishing (1) or legitimate (0) from a single raw record.
    """
    if model_name not in MODELS:
        raise ValueError(f"Model '{model_name}' not found! Choose from {list(MODELS.keys())}")

    model = MODELS[model_name]
    df_prepared = prepare_features_from_raw(record)

    pred = int(model.predict(df_prepared)[0])
    proba = (
        round(float(model.predict_proba(df_prepared)[0][1]), 3)
        if hasattr(model, "predict_proba")
        else None
    )

    return {
        "model": model_name,
        "prediction": "Phishing" if pred == 1 else "Legitimate",
        "raw_label": pred,
        "probability_phishing": proba
    }
