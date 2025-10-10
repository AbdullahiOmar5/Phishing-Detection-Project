
🎓 project_paper.md – Phishing Website Detection
1. Introduction
Phishing websites are a common online threat. Attackers mimic legitimate domains to steal sensitive information. This project builds a machine learning system that predicts whether a website is Phishing or Legitimate based on URL and content-based features.

## 2. 🧩 Dataset Details

- **Source:** kaggle 
- **Samples:** ~11430 rows  
- **Features:** 88  
- **Target Column:** `Result` (1 = Phishing, -1 = Legitimate)


### Preprocessing steps:
-Removed irrelevant/duplicate columns
Cleaned missing values
Scaled all numeric features using StandardScaler
Selected top 20 features using Random Forest importance
Saved scaler and feature list for deployment

## 3. Top 20 Features Used:
['google_index', 'page_rank', 'nb_hyperlinks', 'web_traffic', 'nb_www', 'domain_age', 'ratio_extHyperlinks', 'phish_hints', 'longest_word_path', 'ratio_intHyperlinks', 'safe_anchor', 'length_url', 'ratio_extRedirection', 'ratio_digits_url', 'longest_words_raw', 'length_words_raw', 'length_hostname', 'char_repeat', 'avg_word_path', 'links_in_tags']

## 3. Algorithms Used
We trained three algorithms:

- **Logistic Regression** – baseline linear model  
- **Decision Tree Classifier** – interpretable tree-based approach  
- **Random Forest Classifier** – ensemble of trees that achieved the best performance  

## 4. Results

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 91.95%   | 0.9088    | 0.9326 | 0.9206   |
| Decision Tree       | 92.65%   | 0.9228    | 0.9309 | 0.9268   |
| Random Forest       | 95.28%   | 0.9481    | 0.9580 | 0.9530   |

## 5. Sanity Checks (Sample Rows)
    | Row | Actual | LR | RF | DT |
    | --- | ------ | -- | -- | -- |
    | 1   | 1      | 1  | 1  | 1  |
    | 5   | 0      | 0  | 0  | 0  |
    | 10  | 1      | 1  | 1  | 1  |
    | 34  | 1      | 1  | 1  | 1  |



## 6. Deployment
Flask API accepts POST requests to /predict?model=lr|rf|dt
Extracts URL features, scales with saved scaler, and returns prediction with probability

### Example request:
```json
{
  "url": "https://paypal-login-secure-update.com/account"
}

### Example Response:
{
  "model": "rf",
  "prediction": "Phishing",
  "raw_label": 1,
  "probability_phishing": 0.85,
  "url": "https://paypal-login-secure-update.com/account"
}



## 💡 Lessons Learned
How to choose a relavent topic and then search it's dataset.
Proper feature selection and scaling are critical for high accuracy
Random Forest is robust for phishing detection
Unified preprocessing ensures consistency between training and deployment
Flask provides a lightweight, production-ready API
Postman/cURL helps test API endpoints efficiently