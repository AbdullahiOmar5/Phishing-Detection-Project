# 🎓 Phishing Website Detection using Machine Learning

## 👤 Student Information
Name: Abdullahi Omar Hussein
Course: Machine Learning – Final Project
Date: October 10, 2025

## 📘 Project Overview
🔍 Project Title
Phishing Website Detection using Machine Learning
🧠 Description
Phishing attacks remain one of the most common cyber threats worldwide.
Malicious actors often create deceptive websites to steal sensitive user information such as login credentials or financial details.
This project leverages machine learning models to classify websites as Phishing or Legitimate using 25 URL-based features.
It integrates a Flask API backend with a modern React + Vite frontend, providing a real-time web interface for URL evaluation and visualization of model predictions.
---

## 🗂️ Project Structure
phishing-detection project/
│
├── dataset/
|   ├── raw/       
|   |     └── dataset_phishing.csv
│   ├──processed/
|           ├── phishing_cleaned_dataset.csv  
|           ├── phishing_test_scaled.csv
|           ├── phishing_train_scaled.csv   

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
|
├── notebooks/
│   ├── exploration.ipynb
|
├── frontend/                    # React + Vite UI (Tailwind + Framer Motion)
│   ├── src/
│   │   ├── pages/               # Home, Predict, About
│   │   ├── components/          # Header, Footer, UrlCard, etc.
│   │   └── styles/
│   │       └── globals.css
│   └── package.json
|
├── project_paper.md
└── README.md


---

## 🧩 Dataset Details

- **Source:** kaggle 
- **Samples:** ~11430 rows  
- **Features:** 88  
- **Features Used:** Top 25 most important features
- **Target Column:** `Result` (1 = Phishing, -1 = Legitimate)

### ⚙️ Preprocessing Steps
- Removed irrelevant or duplicate columns  
- Normalized numerical features  
- Selected top 25 features using Random Forest importance ranking  
- Scaled features using `StandardScaler`
- Applied StandardScaler for feature normalization  
- Saved processed data and scaler for model training and deployment 
- Stored scaler.pkl and top25_features.json for consistent API inference 

---

## 🤖 Machine Learning Models & Results

| Model               | Accuracy   | Precision  | Recall     | F1-Score   |
| ------------------- | ---------- | ---------- | ---------- | ---------- |
| Logistic Regression | 0.7918     | 0.8191     | 0.7489     | 0.7824     |
| Decision Tree       | 0.8329     | 0.8513     | 0.8066     | 0.8284     |
| Random Forest       | 0.8613     | 0.8701     | 0.8495     | 0.8597     |




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

- **POST** /predict?model=lr|rf|dt

| Query Parameter | Model Name          |
| ----------------| ------------------- |
| lr              | Logistic Regression |
| rf              | Random Forest       |
| dt              | Decision Tree       |

---

#### 🔹 Request

```json
{
  "url": "https://paypal-login-secure-update.com/account"
}
```

### 🔹 Response
```json
{
  "url": "https://paypal-login-secure-update.com/account",
  "results": [
    {"model": "random_forest", "prediction": "Phishing", "raw_label": 1, "probability_phishing": 0.93},
    {"model": "logistic_regression", "prediction": "Phishing", "raw_label": 1, "probability_phishing": 0.84},
    {"model": "decision_tree", "prediction": "Phishing", "raw_label": 1, "probability_phishing": 1.0}
  ]
}
```

  


## Frontend: React + Vite UI

### Overview
A responsive and polished web UI was developed for interacting with the ML backend. The frontend provides an easy-to-use interface to submit URLs, select ML models, and inspect predictions.

### Tech stack
- React + Vite (fast dev server)
- Tailwind CSS for styling
- Framer Motion for animations
- react-icons (icons)
- Axios or fetch for API requests
- Optional: shadcn/ui for prebuilt components

### Pages & Components
- `Home` — hero header, subtitle, two CTA buttons:
  - **Try Demo** → goes to `/predict`
  - **Learn More** → goes to `/about`
- `Predict` — main interaction page:
  - **UrlInputCard**: URL text input + model selector + Analyze button
  - **EvaluationCard**: shows prediction, probability, and model name
  - Loading spinner + friendly error messages for invalid URLs or network errors
- `About` — project description, dataset, methods, author info
- `Header` / `Footer` — navigation and project meta

### How the frontend talks to the API
- Dev default backend URL: `http://127.0.0.1:5001/predict`
- Example request from frontend (POST JSON):
  ```json
  {"url": "https://paypal-login-secure-update.com/account"}
  ```

### Run Frontend:
cd frontend
npm install
npm run dev

### Run Backend:
cd src
python app.py


## 🧾 Results Summary
Best Model: Random Forest Classifier
Accuracy: 85%
Inference Time: < 50 ms per URL
Deployment: Flask API with CORS enabled
Scalability: Easily integrable into web or mobile phishing detection tools

## 💡 Lessons Learned
Feature selection and scaling greatly enhance model accuracy.
Random Forest handled non-linear phishing patterns better than linear models.
A unified preprocessing pipeline streamlined both training and deployment.
Flask provided a simple yet powerful API framework for ML integration.
Postman and cURL proved invaluable for API testing and debugging.
React + Vite enabled a fast, responsive, and visually appealing frontend.

## 📘 References
Kaggle – Phishing Web Page Detection Dataset
UCI Machine Learning Repository – Phishing Websites Dataset
Scikit-learn Documentation
Flask Documentation
Joblib (Model Serialization)
Python Standard Library
Tailwind CSS
React + Vite Documentation


## 🧑‍💻 Author
### Abdullahi Omar Hussein
### Machine Learning Engineer
