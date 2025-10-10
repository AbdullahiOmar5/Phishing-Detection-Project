# 🎓 Final Project – Phishing Website Detection using Machine Learning

## 👤 Student Information
- **Name:** Abdullahi Omar  
- **Course:** Machine Learning – Final Project  
- **Date:** October 10, 2025  

---

## 📘 Project Overview

### 🔍 Project Title
**Phishing Website Detection using Machine Learning**

### 🧠 Description
Phishing attacks are one of the most prevalent cyber threats, where malicious actors create deceptive websites to steal sensitive user information. This project leverages machine learning algorithms to automatically classify websites as either **Phishing** or **Legitimate** based on extracted URL and content-based features.

A trained model is deployed via a **Flask API**, allowing real-time phishing detection by submitting a URL and receiving a prediction response.

---

## 🗂️ Project Structure
phishing-detector/ │ ├── dataset/ │ └── dataset_phishing.csv │ ├── src/ │ ├── processing.py │ ├── train_models.py │ ├── utils.py │ ├── test_prediction.py │ └── app.py │ ├── models/ │ ├── Logistic Regression.pkl │ ├── Random Forest.pkl │ ├── Decision Tree.pkl │ ├── scaler.pkl │ └── top20_features.json │ ├── README.md └── project_paper.md


---

## 🧩 Dataset Details

- **Source:** UCI Machine Learning Repository  
- **Samples:** ~11,055 rows  
- **Features:** 30  
- **Target Column:** `Result` (1 = Phishing, -1 = Legitimate)

### ⚙️ Preprocessing Steps
- Removed irrelevant or duplicate columns  
- Normalized numerical features  
- Selected top 20 features using Random Forest feature importance  
- Scaled features using `StandardScaler`  
- Saved processed data and scaler for model training and deployment  

---

## 🤖 Algorithms Used

| Algorithm               | Type            | Key Parameters                     | Accuracy | F1 Score |
|------------------------|-----------------|------------------------------------|----------|----------|
| Logistic Regression     | Linear Model     | `C=1.0`, `max_iter=500`             | 93%      | 0.93     |
| Random Forest Classifier| Ensemble Model   | `n_estimators=200`, `max_depth=10` | 96%      | 0.96     |
| Decision Tree Classifier| Tree Model       | `max_depth=8`                       | 94%      | 0.94     |

---

## 📊 Evaluation & Sanity Checks

| URL                                      | Expected    | Predicted   | Probability (Phishing) |
|------------------------------------------|-------------|-------------|-------------------------|
| paypal-login-secure-update.com           | Phishing    | Phishing    | 0.85                    |
| www.google.com                           | Legitimate  | Legitimate  | 0.03                    |
| secure-update-amazon-support.com         | Phishing    | Phishing    | 0.91                    |

---

## 🚀 Deployment

### ✅ Framework
- Flask (Python)

### 🔌 API Endpoint
- **POST** `/predict`

#### 🔹 Request
```json
{
  "url": "https://paypal-login-secure-update.com/account"
}
🔹 Response
{
  "model": "random_forest",
  "prediction": "Phishing",
  "raw_label": 1,
  "probability_phishing": 0.85,
  "url": "https://paypal-login-secure-update.com/account"
}
🔹 Example with cURL
curl -X POST http://127.0.0.1:5001/predict \
  -H "Content-Type: application/json" \
  -d '{"url": "https://paypal-login-secure-update.com/account"}'
💻 Example Commands
Task	Command
Preprocess data	python src/processing.py
Train models	python src/train_models.py
Test predictions	python src/test_prediction.py
Run API locally	python src/app.py

🧾 Results Summary
Best Model: Random Forest Classifier
Accuracy: 96%
Inference Time: < 50 ms per URL
Deployment: Flask API with CORS enabled
Scalability: Easily integrable into web or mobile phishing detection tools

💡 Lessons Learned
Feature selection and scaling significantly improve model performance
Random Forest outperforms linear models in non-linear classification tasks
A unified preprocessing pipeline simplifies deployment
Flask is effective for lightweight ML API deployment
Tools like Postman and cURL are essential for testing and debugging APIs

📘 References
UCI ML Repository – Phishing Websites Dataset
Scikit-Learn Documentation
Flask Documentation
Joblib for Model Serialization
<<<<<<< HEAD
Python Standard Library
=======
Python Standard Library
>>>>>>> ba27ddc (update project_paper.md)
