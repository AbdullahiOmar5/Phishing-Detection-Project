🎓 README.md – Phishing Website Detection using ML
👤 Student Information
Name: Abdullahi Omar Hussein
Course: Machine Learning – Final Project
Date: October 10, 2025
📘 Project Overview
🔍 Project Title
Phishing Website Detection using Machine Learning
🧠 Description
Phishing attacks are one of the most prevalent cyber threats. Malicious actors create deceptive websites to steal sensitive user information. This project leverages machine learning algorithms to automatically classify websites as Phishing or Legitimate based on URL and content-based features.
A trained model is deployed via a Flask API, allowing real-time phishing detection by submitting a URL and selecting a model.
---

## 🗂️ Project Structure
phishing-detection project/
│
├── dataset/
|   ├── raw       
|   |     └── dataset_phishing.csv
│   ├──processed      
|        └── phishing_cleaned_dataset.csv
│
├── src/
│   ├── processing.py          # Data preprocessing and feature engineering
│   ├── train_models.py        # Model training (LR, RF, DT)
│   ├── utils.py               # Helper functions (feature extraction, prediction)
│   ├── test_prediction.py     # Local test for predictions
|   ├── feature_extractor.py   # Extract dat to for predictions
│   └── app.py                 # Flask API for deployment
│
├── models/
│   ├── Logistic_Regression_top20.pkl
│   ├── Random_Forest_top20.pkl
│   ├── Decision_Tree_top20.pkl
│   ├── scaler.pkl
│   └── top20_features.json
|notebooks/
│   ├── exploration.ipynb
├── project_paper.md
└── README.md


---

## 🧩 Dataset Details

- **Source:** kaggle 
- **Samples:** ~11430 rows  
- **Features:** 88  
- **Target Column:** `Result` (1 = Phishing, -1 = Legitimate)

### ⚙️ Preprocessing Steps
- Removed irrelevant or duplicate columns  
- Normalized numerical features  
- Selected top 20 features using Random Forest feature importance  
- Scaled features using `StandardScaler`  
- Saved processed data and scaler for model training and deployment  

---

## 🤖 Algorithms & Results

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 91.95%   | 0.9088    | 0.9326 | 0.9206   |
| Decision Tree       | 92.65%   | 0.9228    | 0.9309 | 0.9268   |
| Random Forest       | 95.28%   | 0.9481    | 0.9580 | 0.9530   |



## 📊 Sanity Checks

| Row | Actual | Logistic Regression | Random Forest | Decision Tree |
| --- | ------ | ------------------- | ------------- | ------------- |
| 1   | 1      | 1                   | 1             | 1             |
| 5   | 0      | 0                   | 0             | 0             |
| 10  | 1      | 1                   | 1             | 1             |
| 34  | 1      | 1                   | 1             | 1             |



## 🚀 Deployment

### ✅ Framework
- Flask (Python) with CORS enabled

### 🔌 API Endpoint

- **POST** `/predict?model=lr|rf|dt`  
  Query Parameter `model`:  
  - `lr` = Logistic Regression  
  - `rf` = Random Forest  
  - `dt` = Decision Tree  

---

#### 🔹 Request

```json
{
  "url": "https://paypal-login-secure-update.com/account"
}


🔹 Response
{
  "model": "rf",
  "prediction": "Phishing",
  "raw_label": 1,
  "probability_phishing": 0.85,
  "url": "https://paypal-login-secure-update.com/account"
}


🔹 Example with cURL
curl -X POST "http://127.0.0.1:5001/predict?model=rf" \
-H "Content-Type: application/json" \
-d '{"url": "https://paypal-login-secure-update.com/account"}'


🔹 Example with Postman
Method: POST
URL: http://127.0.0.1:5001/predict?model=rf
Header: Content-Type: application/json
Body (raw JSON):
{
  "url": "https://paypal-login-secure-update.com/account"
}
  
💻 Example Commands
| Task                  |               Command                       |
| ----------------------| ------------------------------------------- |
| reprocess data        |               python src/processing.py      |
| Train models          |               python src/train_models.py    |
| Test predictions      |               python src/test_prediction.py |
| Run API               |               python src/app.py             |



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
Kaggle - Phishing Web page phishing detection
UCI ML Repository – Phishing Websites Dataset
Scikit-Learn Documentation
Flask Documentation
Joblib for Model Serialization
Python Standard Library

