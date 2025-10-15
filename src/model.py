# model.py (Final Version – Metrics Summary + Sanity Check for All Models)

import pandas as pd
import joblib
import os
import json
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay
)

# === 1️⃣ Load preprocessed datasets ===
TRAIN_PATH = "../dataset/processed/phishing_train_scaled.csv"
TEST_PATH = "../dataset/processed/phishing_test_scaled.csv"

df_train = pd.read_csv(TRAIN_PATH)
df_test = pd.read_csv(TEST_PATH)
print("✅ Loaded train/test datasets")
print(f"Train: {df_train.shape}, Test: {df_test.shape}")

# === 2️⃣ Load selected 25 features ===
FEATURES_PATH = "../models/final_features.json"
with open(FEATURES_PATH, "r") as f:
    final_features = json.load(f)

TARGET_COL = "status"

# === 3️⃣ Prepare data ===
X_train = df_train[final_features]
y_train = df_train[TARGET_COL]

X_test = df_test[final_features]
y_test = df_test[TARGET_COL]

# === 4️⃣ Define models ===
models = {
    "Logistic Regression": LogisticRegression(max_iter=10000, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42)
}

# === 5️⃣ Helper: Evaluate model ===
def evaluate_model(y_true, y_pred):
    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
        "F1-Score": f1_score(y_true, y_pred)
    }

# === 6️⃣ Train, evaluate, and save models ===
os.makedirs("../models", exist_ok=True)
results = {}
predictions_dict = {}

for name, model in models.items():
    print(f"\n🚀 Training {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Evaluate
    metrics = evaluate_model(y_test, y_pred)
    results[name] = metrics
    predictions_dict[name] = model

    # Print metrics
    print(f"\n{name} Performance:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(cm, display_labels=["Legitimate", "Phishing"])
    disp.plot(cmap="Blues")
    plt.title(f"{name} Confusion Matrix")
    plt.show()

    # Save model
    model_filename = f"{name.replace(' ', '_')}_25.pkl"
    joblib.dump(model, f"../models/{model_filename}")
    print(f"💾 Saved {name} model to ../models/{model_filename}")

print("\n✅ All models trained, evaluated, and saved successfully!")

# === 7️⃣ Metrics Summary Table ===
results_df = pd.DataFrame(results).T
results_df = results_df.sort_values(by="Accuracy", ascending=False)
print("\n📊 Model Performance Summary:\n")
print(results_df.to_string(index=True, float_format="%.4f"))

# === 8️⃣ Sanity Check for All Models ===
sanity_rows = [1, 5, 10, 34]
print("\n🔍 Sanity Check (Rows 1, 5, 10, 34):\n")

for name, model in predictions_dict.items():
    print(f"🧠 {name} Predictions:")
    sanity_data = X_test.iloc[sanity_rows]
    sanity_labels = y_test.iloc[sanity_rows].values
    sanity_preds = model.predict(sanity_data)

    sanity_df = pd.DataFrame({
        "Row Index": sanity_rows,
        "Actual": sanity_labels,
        "Predicted": sanity_preds
    })

    print(sanity_df.to_string(index=False))
    print("-" * 50)
