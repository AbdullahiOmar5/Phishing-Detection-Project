# preprocessing.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import os
import joblib
import json

# === 1️⃣ Load Raw Dataset ===
RAW_PATH = "../dataset/raw/dataset_phishing.csv"
df = pd.read_csv(RAW_PATH)
print("Initial shape:", df.shape)

# === 2️⃣ Basic Cleaning ===
# Drop 'url' column (textual)
if 'url' in df.columns:
    df.drop('url', axis=1, inplace=True)

# Drop unnamed index columns (if any)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Drop rows with missing values
df = df.dropna()
print("After cleaning shape:", df.shape)
print("Columns:", df.columns.tolist()[:10], "...")  # preview first few columns

# === 3️⃣ Encode Target Column ===
TARGET_COL = 'status'
if df[TARGET_COL].dtype == object:
    df[TARGET_COL] = df[TARGET_COL].str.lower().map({
        'legitimate': 0,
        'benign': 0,
        'phishing': 1,
        'malicious': 1
    })
df[TARGET_COL] = df[TARGET_COL].astype(int)
print("Target value counts:\n", df[TARGET_COL].value_counts())

# === 4️⃣ Separate Features and Target ===
X = df.drop(TARGET_COL, axis=1)
y = df[TARGET_COL]

# === 5️⃣ Feature Scaling ===
scaler_full = StandardScaler()
X_scaled_full = scaler_full.fit_transform(X)

# Create scaled DataFrame
df_scaled_full = pd.DataFrame(X_scaled_full, columns=X.columns)
df_scaled_full[TARGET_COL] = y.values

# === 6️⃣ Create Output Folders ===
os.makedirs("../dataset/processed", exist_ok=True)
os.makedirs("../models", exist_ok=True)

# === 7️⃣ Save Processed Files ===
CLEANED_PATH = "../dataset/processed/phishing_cleaned_dataset.csv"
SCALER_PATH = "../models/scaler.pkl"
FEATURES_PATH = "../models/training_features.json"

df_scaled_full.to_csv(CLEANED_PATH, index=False)
joblib.dump(scaler_full, SCALER_PATH)
json.dump(list(X.columns), open(FEATURES_PATH, 'w'))

print("\n✅ Full preprocessing complete!")
print(f"Cleaned dataset saved to: {CLEANED_PATH}")
print(f"Full scaler saved to: {SCALER_PATH}")
print(f"Feature list saved to: {FEATURES_PATH}")
print("Final shape:", df_scaled_full.shape)

# === 8️⃣ Compute Top 20 Features ===
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X, y)
importances = pd.Series(rf.feature_importances_, index=X.columns)
top20_features = importances.sort_values(ascending=False).head(20).index.tolist()

# Save top 20 features
TOP_FEATURES_PATH = "../models/top20_features.json"
json.dump(top20_features, open(TOP_FEATURES_PATH, 'w'))
print("\n✅ Top 20 features saved to:", top20_features)

# === 9️⃣ Create Scaler for Top 20 Features ===
X_top20 = X[top20_features]
scaler_top20 = StandardScaler()
scaler_top20.fit(X_top20)
SCALER_TOP20_PATH = "../models/scaler_top20.pkl"
joblib.dump(scaler_top20, SCALER_TOP20_PATH)
print("✅ Scaler for top 20 features saved:", SCALER_TOP20_PATH)
