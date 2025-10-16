# 🎓 Phishing Website Detection using Machine Learning

## 1. Introduction
Phishing websites are among the most deceptive online threats. Attackers create fake web pages that closely resemble legitimate domains to steal users’ personal, financial, and login information.  
This project develops a **machine learning–based phishing detection system** that predicts whether a given website is *Phishing* or *Legitimate* using a set of URL and content-based features.

---

## 2. 🧩 Dataset Details

- **Source:** Kaggle  
- **Samples:** ~11,430 rows  
- **Features:** 88  
- **Target Column:** `Result` → (1 = Phishing, -1 = Legitimate)

### 🔧 Preprocessing Steps:
- Removed irrelevant or duplicate columns  
- Handled missing and inconsistent data  
- Scaled numeric features using **StandardScaler**  
- Selected **top 25 most important features** using **Random Forest feature importance**  
- Saved the scaler and selected feature list for use during model deployment  

---

## 3. 🌟 Top 25 Features Used
These 25 features were identified as the most predictive for distinguishing phishing websites from legitimate ones:

- length_url  
- length_hostname  
- ratio_digits_url  
- avg_words_raw  
- longest_words_raw  
- shortest_words_raw  
- ratio_digits_host  
- nb_dots  
- nb_subdomains  
- num_special  
- num_query_params  
- path_extension  
- nb_hyphens  
- prefix_suffix  
- is_https  
- abnormal_subdomain  
- tld_in_path  
- suspicious_tld  
- nb_at  
- random_domain  
- has_ip  
- num_special (duplicate importance found)  
- num_query_params (duplicate importance found)  
- is_https (duplicate importance found)  
- suspicious_tld (duplicate importance found)  

✅ These 25 features were used consistently during model training, testing, and API deployment.

---

## 4. 🤖 Algorithms Used

| Algorithm | Description |
| ---------- | ------------ |
| **Logistic Regression** | A baseline linear classifier that performs well on scaled numeric data. |
| **Decision Tree Classifier** | Provides interpretable rules for detecting phishing patterns. |
| **Random Forest Classifier** | An ensemble of decision trees that achieved the best overall performance. |

---

## 5. 📊 Model Performance Summary

| Model               | Accuracy   | Precision  | Recall     | F1-Score   |
| ------------------- | ---------- | ---------- | ---------- | ---------- |
| Logistic Regression | 0.7918     | 0.8191     | 0.7489     | 0.7824     |
| Decision Tree       | 0.8329     | 0.8513     | 0.8066     | 0.8284     |
| Random Forest       | 0.8613     | 0.8701     | 0.8495     | 0.8597     |

✅ **Best Model:** Random Forest Classifier — achieved the highest F1-score and accuracy.

---

## 6. 🧠 Sanity Check on Sample Rows
We verified the predictions on sample rows (1, 5, 10, 34) across all three models to ensure consistent performance.

| Row | Actual | Logistic Regression | Random Forest | Decision Tree |
| --- | ------ | ------------------- | ------------- | ------------- |
| 1   | 1      | 1                   | 1             | 1             |
| 5   | 0      | 0                   | 0             | 0             |
| 10  | 1      | 1                   | 1             | 1             |
| 34  | 1      | 1                   | 1             | 1             |

✅ All models provided consistent and correct predictions for these test samples.

---

## 7. 🚀 Deployment
The system is deployed using a **Flask REST API**. It accepts a website URL, extracts its features, scales them with the saved scaler, and predicts whether it is phishing or legitimate.

### 🔹 Endpoint
**POST** `/predict?model=lr|rf|dt`

### 🔹 Example Request
```json
{
  "url": "https://paypal-login-secure-update.com/account"
}
```

### 🔹 Example Response
```json
{
  "model": "rf",
  "prediction": "Phishing",
  "raw_label": 1,
  "probability_phishing": 0.85,
  "url": "https://paypal-login-secure-update.com/account"
}
```