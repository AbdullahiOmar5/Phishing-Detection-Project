🎓 Final Project – Phishing Website Detection using Machine Learning
👤 Student Information
Name: Abdullahi Omar
Course: Machine Learning – Final Project
Date: October 10, 2025
📘 Project Overview
🔍 Project Title
Phishing Website Detection using Machine Learning
🧠 Description
This project aims to automatically detect phishing websites using machine learning algorithms. Phishing attacks are among the most common forms of cybercrime, where attackers create fake websites to steal user information.
We trained and deployed machine learning models to classify a given URL as “Phishing” or “Legitimate.”
The model is accessible through a Flask API that accepts a website URL and returns a prediction.
🗂️ Project Structure
phishing-detector/
│
├── dataset/
│   └── dataset_phishing.csv
│
├── src/
│   ├── processing.py          # Data preprocessing and feature engineering
│   ├── train_models.py        # Model training (Logistic Regression, Random Forest, Decision Tree)
│   ├── utils.py               # Helper functions (feature extraction, prediction)
│   ├── test_prediction.py     # Local test for predictions
│   └── app.py                 # Flask API for deployment
│
├── models/
│   ├── Logistic Regression.pkl
│   ├── Random Forest.pkl
│   ├── Decision Tree.pkl
│   ├── scaler.pkl
│   └── top20_features.json
│
├── README.md
└── project_paper.md
🧩 Dataset Details
📊 Dataset Source
Dataset Name: Phishing Websites Dataset
Source: UCI Machine Learning Repository
Samples: ~11,055 rows
Features: 30
Target Column: Result (1 = Phishing, -1 = Legitimate)
⚙️ Preprocessing Steps
Removed irrelevant or duplicate columns
Normalized numerical features
Selected top 20 features using feature importance (Random Forest)
Scaled selected features using StandardScaler
Saved processed data for model training and API inference
🤖 Algorithms Used
Algorithm	Type	Key Parameters	Accuracy	F1 Score
Logistic Regression	Linear Model	C=1.0, max_iter=500	93%	0.93
Random Forest Classifier	Ensemble Model	n_estimators=200, max_depth=10	96%	0.96
Decision Tree Classifier	Tree Model	max_depth=8	94%	0.94
🏆 Best Model
Random Forest Classifier achieved the highest accuracy and generalization performance.
📊 Evaluation & Sanity Checks
Example predictions (from test set):
URL	Expected	Predicted	Probability (Phishing)
paypal-login-secure-update.com	Phishing	Phishing	0.85
www.google.com	Legitimate	Legitimate	0.03
secure-update-amazon-support.com	Phishing	Phishing	0.91
🚀 Deployment
✅ Framework
Flask (Python)
🔌 API Endpoint
POST /predict
🔹 Request
URL:
http://127.0.0.1:5001/predict
Body (JSON):
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
🔹 Example with Postman
Method: POST
URL: http://127.0.0.1:5001/predict
Header: Content-Type: application/json
Body (raw JSON):
{
  "url": "https://paypal-login-secure-update.com/account"
}
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
Scalability: Can easily integrate into web or mobile phishing detection tools.
💡 Lessons Learned
Data preprocessing (feature selection + scaling) greatly improves performance.
Random Forest outperforms simple linear models in non-linear classification.
Building a unified preprocessing pipeline simplifies model deployment.
Flask provides a fast and reliable API deployment for ML models.
Interfacing Postman and Python helped validate inference behavior.
📘 References
UCI Machine Learning Repository: Phishing Websites Dataset
Scikit-Learn Documentation
Flask Documentation
Joblib for Model Serialization
Python Standard Library
