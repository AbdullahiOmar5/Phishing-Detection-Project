# batch_test.py
import pandas as pd
from feature_extractor import extract_features_from_url_extended
from utils import predict_phishing
import os

# Put your test URLs here (legit + phishing)
urls = [
    # Legitimate
    "https://www.apple.com/",
    "https://www.google.com/",
    "https://github.com/",
    "https://www.bankofamerica.com/",
    "https://www.wikipedia.org/",
    "https://www.nytimes.com/",
    "https://www.microsoft.com/",
    "https://www.amazon.com/",
    "https://www.bbc.co.uk/",
    "https://stackoverflow.com/questions",
    # Phishing
    "http://secure-paypal-account-login.xyz",
    "http://login-paypal-secure.xyz",
    "http://appleid.apple.com-app.es/",
    "http://update-google-account.verify-login.info/",
    "http://bankofamerica.login.verify-online.top/",
    "http://secure-login-gmail.com/",
    "http://free-gift-amazon-prize.online/claim",
    "http://bit.ly/secure-login-123",
    "http://123.45.67.89/verify",
    "http://paypal.support.account.verify.online/login"
]

rows = []
models = ["logistic_regression", "random_forest", "decision_tree"]

for url in urls:
    # Extract features for URL
    features = extract_features_from_url_extended(url)

    # Add original url for inspection
    row = {"url": url}
    # run predictions for each model
    for m in models:
        try:
            res = predict_phishing(features, model_name=m)
            row[f"{m}_pred"] = res["prediction"]
            row[f"{m}_raw"] = res["raw_label"]
            row[f"{m}_prob"] = res["probability_phishing"]
        except Exception as e:
            row[f"{m}_pred"] = None
            row[f"{m}_raw"] = None
            row[f"{m}_prob"] = None
            row[f"{m}_error"] = str(e)
    rows.append(row)

df_results = pd.DataFrame(rows)

# Pretty print
pd.set_option('display.max_columns', None)
print(df_results)

