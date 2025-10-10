
# 🎓 Project Paper – Phishing Website Detection

## 1. Introduction
Phishing websites are one of the most common online threats. Attackers mimic legitimate domains to trick users into providing sensitive data. This project builds a machine learning-based system to automatically detect phishing websites based on URL and content features.

## 2. Dataset & Preprocessing
We used the Phishing Websites Dataset from the UCI ML Repository with 11,055 samples and 30 attributes.

### Preprocessing steps:
- Cleaned and encoded categorical features  
- Scaled numerical values using StandardScaler  
- Selected the top 20 most important features  
- Saved preprocessing pipeline for use in deployment  

## 3. Algorithms Used
We trained three algorithms:

- **Logistic Regression** – baseline linear model  
- **Decision Tree Classifier** – interpretable tree-based approach  
- **Random Forest Classifier** – ensemble of trees that achieved the best performance  

## 4. Results

| Model              | Accuracy | F1 Score |
|--------------------|----------|----------|
| Logistic Regression| 93%      | 0.93     |
| Decision Tree      | 94%      | 0.94     |
| Random Forest      | 96%      | 0.96     |

Random Forest was selected as the deployment model.

## 5. Deployment
We built a Flask API to serve the trained Random Forest model.

### Example:
```json
{
  "url": "https://paypal-login-secure-update.com/account",
  "prediction": "Phishing",
  "probability_phishing": 0.85
}
## 6. Lessons Learned

This project taught me the end-to-end workflow of an ML system — from dataset cleaning, model comparison, and feature selection, to deploying a real API.
Key takeaways:
Data preprocessing is crucial
Random Forest provides strong baseline accuracy
Flask enables lightweight deployment for testing and integration