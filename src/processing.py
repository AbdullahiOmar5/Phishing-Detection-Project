# preprocessing.py (Updated for 25 features)
import pandas as pd
import os
import json
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from feature_extractor import extract_features_from_url_extended

# === 1️⃣ Load Raw Dataset ===
RAW_PATH = "../dataset/raw/dataset_phishing.csv"
df_raw = pd.read_csv(RAW_PATH)
print("Initial dataset shape:", df_raw.shape)

# === 2️⃣ Basic Cleaning ===
df_raw = df_raw.dropna(subset=['url', 'status'])
print("After dropping missing URLs/status:", df_raw.shape)

# === 3️⃣ Encode Target Column ===
TARGET_COL = 'status'
if df_raw[TARGET_COL].dtype == object:
    df_raw[TARGET_COL] = df_raw[TARGET_COL].str.lower().map({
        'legitimate': 0,
        'phishing': 1,
    })
df_raw[TARGET_COL] = df_raw[TARGET_COL].astype(int)
print("Target distribution:\n", df_raw[TARGET_COL].value_counts(normalize=True))

# === 4️⃣ Extract Features from URLs ===
print("Extracting features from URLs...")
feature_dicts = df_raw['url'].apply(lambda u: extract_features_from_url_extended(u))
df_features = pd.DataFrame(list(feature_dicts))
print("Extracted feature columns:", df_features.columns.tolist())

# === 5️⃣ Combine features and target ===
df = pd.concat([df_features, df_raw[TARGET_COL]], axis=1)
print("Shape after feature extraction:", df.shape)

# === 6️⃣ Define final 25 features ===
TOP_FEATURES_PATH = "../models/top20_features.json"
with open(TOP_FEATURES_PATH, "r") as f:
    top20_features = json.load(f)

extended_features = [
    "is_https",
    "has_ip",
    "num_query_params",
    "num_special",
    "suspicious_tld"
]

final_features = top20_features + extended_features
print("✅ Using final 25 features:", final_features)

# Defensive: fill missing columns if any
for col in final_features:
    if col not in df.columns:
        df[col] = 0.0

# === 7️⃣ Split into features & target ===
X = df[final_features]
y = df[TARGET_COL]

# === 8️⃣ Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")

# === 9️⃣ Feature Scaling ===
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert back to DataFrame for saving
df_train_scaled = pd.DataFrame(X_train_scaled, columns=final_features)
df_train_scaled[TARGET_COL] = y_train.values

df_test_scaled = pd.DataFrame(X_test_scaled, columns=final_features)
df_test_scaled[TARGET_COL] = y_test.values

# === 1️⃣ 0️⃣ Create output folders ===
os.makedirs("../dataset/processed", exist_ok=True)
os.makedirs("../models", exist_ok=True)

# === 1️⃣ 1️⃣ Save processed datasets and scaler ===
TRAIN_PATH = "../dataset/processed/phishing_train_scaled.csv"
TEST_PATH = "../dataset/processed/phishing_test_scaled.csv"
SCALER_PATH = "../models/scaler_25_features.pkl"
FEATURES_PATH = "../models/final_features.json"

df_train_scaled.to_csv(TRAIN_PATH, index=False)
df_test_scaled.to_csv(TEST_PATH, index=False)
joblib.dump(scaler, SCALER_PATH)
json.dump(final_features, open(FEATURES_PATH, "w"))

print("\n✅ Preprocessing complete!")
print(f"Train dataset saved to: {TRAIN_PATH}")
print(f"Test dataset saved to: {TEST_PATH}")
print(f"Scaler saved to: {SCALER_PATH}")
print(f"Final features saved to: {FEATURES_PATH}")

# === 1️⃣ 2️⃣ Compute feature importance (optional) ===
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
importances = pd.Series(rf.feature_importances_, index=final_features)
top_features_sorted = importances.sort_values(ascending=False)
print("\nTop 25 features by importance:")
print(top_features_sorted)
