# utils.py (Updated for 25 features)
import json
import joblib
import pandas as pd
import os

# ===========================
# 🔧 Load Pre-Fitted Objects
# ===========================

# Scaler for 25 features
SCALER_PATH = "../models/scaler_25_features.pkl"
if not os.path.exists(SCALER_PATH):
    raise FileNotFoundError(f"Scaler file not found at {SCALER_PATH}")
SCALER = joblib.load(SCALER_PATH)

# Final 25 features
FEATURES_PATH = "../models/final_features.json"
if not os.path.exists(FEATURES_PATH):
    raise FileNotFoundError(f"Final features file not found at {FEATURES_PATH}")
FINAL_FEATURES = json.load(open(FEATURES_PATH))

# Trained models
MODEL_PATHS = {
    "logistic_regression": "../models/Logistic_Regression_25.pkl",
    "random_forest": "../models/Random_Forest_25.pkl",
    "decision_tree": "../models/Decision_Tree_25.pkl"
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
    Prepare a single URL record for phishing prediction.
    - Uses exactly the final 25 features
    - Fills missing features with 0
    - Applies the saved scaler
    """
    row = {col: 0.0 for col in FINAL_FEATURES}

    for name, val in record.items():
        if name in row:
            try:
                row[name] = float(val)
            except:
                row[name] = 0.0

    df_one = pd.DataFrame([row], columns=FINAL_FEATURES)
    df_scaled = pd.DataFrame(SCALER.transform(df_one), columns=FINAL_FEATURES)
    return df_scaled

# ===========================
# 🔮 Prediction Function
# ===========================
def predict_phishing(record: dict, model_name: str = "random_forest") -> dict:
    """
    Predict phishing (1) or legitimate (0) using trained 25-feature models.
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
