# test_prediction.py
from utils import predict_phishing

# =========================================================
# 🧩 Sample Record — must include only the top 20 features
# =========================================================
sample_record = {
    "length_url": 45,
    "length_hostname": 18,
    "nb_dots": 2,
    "nb_hyphens": 1,
    "nb_at": 0,
    "ratio_digits_url": 0.15,
    "ratio_digits_host": 0.02,
    "shortest_words_raw": 3,
    "longest_words_raw": 10,
    "avg_words_raw": 4.5,
    "tld_in_path": 0,
    "abnormal_subdomain": 1,
    "nb_subdomains": 2,
    "prefix_suffix": 0,
    "random_domain": 0,
    "shortening_service": 0,
    "path_extension": 1,
    "nb_redirection": 0,
    "ratio_extHyperlinks": 0.05,
    "ratio_intErrors": 0.0
}

# =========================================================
# 🔮 Test predictions using all 3 models
# =========================================================

print("🔹 Testing sample phishing prediction...\n")

# Random Forest
result_rf = predict_phishing(sample_record, model_name="random_forest")
print("🌲 Random Forest Prediction:", result_rf)

# Logistic Regression
result_lr = predict_phishing(sample_record, model_name="logistic_regression")
print("\n📈 Logistic Regression Prediction:", result_lr)

# Decision Tree
result_dt = predict_phishing(sample_record, model_name="decision_tree")
print("\n🌳 Decision Tree Prediction:", result_dt)
