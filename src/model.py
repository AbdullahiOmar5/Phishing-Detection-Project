import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay
)
import json

# === 1️⃣ Load preprocessed data ===
path = '../dataset/processed/phishing_cleaned_dataset.csv'
df = pd.read_csv(path)
print("Loaded cleaned data:", df.shape)

# === 2️⃣ Load top 20 features ===
top_features_path = '../models/top20_features.json'
with open(top_features_path, 'r') as f:
    top_features = json.load(f)

print("Top 20 features being used:", top_features)

# === 3️⃣ Split into features & target ===
TARGET_COL = 'status'
X = df[top_features]  # only top 20 features
y = df[TARGET_COL]

# === 4️⃣ Train-test split ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# === 5️⃣ Define models ===
models = {
    "Logistic Regression": LogisticRegression(max_iter=10000, random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42)
}

# === 6️⃣ Helper functions ===
def evaluate_model(y_true, y_pred):
    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
        "F1-Score": f1_score(y_true, y_pred)
    }

def plot_confusion_matrix(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(f"\nConfusion Matrix for {model_name}:\n", cm)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap='Blues', colorbar=True)
    plt.title(f"{model_name} - Confusion Matrix")
    plt.show()

# === 7️⃣ Train and evaluate ===
results = {}
for name, model in models.items():
    print(f"\n🚀 Training {name} on top 20 features...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    metrics = evaluate_model(y_test, y_pred)
    results[name] = metrics

    print(f"\n{name} Results:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

    plot_confusion_matrix(model, X_test, y_test, name)

# === 8️⃣ Sanity checks for a few test rows ===
print("\n🔍 Sanity Check on Sample Predictions (0 = Legitimate, 1 = Phishing):")
indices_to_check = [1, 5, 10, 34]

for i in indices_to_check:
    x_one_df = X_test.iloc[[i]]
    y_true = y_test.iloc[i]

    preds = {name: int(model.predict(x_one_df)[0]) for name, model in models.items()}

    print(f"\n🧩 Row index {i}:")
    print(f"  Actual Label : {y_true}")
    for name, pred in preds.items():
        print(f"  {name:18}: Predicted = {pred}")

# === 9️⃣ Save models ===
for name, model in models.items():
    model_path = f'../models/{name.replace(" ", "_")}_top20.pkl'
    joblib.dump(model, model_path)
    print(f"Saved {name} model (top 20 features) to {model_path}")
