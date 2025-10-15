# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import predict_phishing
from feature_extractor import extract_features_from_url_extended

app = Flask(__name__)
CORS(app)

# ===========================
# 🔹 Home endpoint
# ===========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "🌐 Phishing Website Detection API",
        "usage": "Send POST request to /predict with {'url': 'https://example.com'}",
        "example_request": {"url": "https://paypal-login-secure-update.com/account"},
        "example_response": {
            "url": "https://paypal-login-secure-update.com/account",
            "results": [
                {"model": "random_forest", "prediction": "Phishing", "raw_label": 1, "probability_phishing": 0.85},
                {"model": "logistic_regression", "prediction": "Legitimate", "raw_label": 0, "probability_phishing": 0.4},
                {"model": "decision_tree", "prediction": "Phishing", "raw_label": 1, "probability_phishing": 1.0}
            ]
        }
    })

# ===========================
# 🔮 Predict endpoint
# ===========================
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    url = data.get("url")
    if not url:
        return jsonify({"error": "Missing 'url' field in JSON payload"}), 400

    # Optional: client can request a specific model via query param ?model=lr|rf|dt
    requested_model = request.args.get('model')

    try:
        # 1️⃣ Extract features from URL
        features = extract_features_from_url_extended(url)

        # 2️⃣ Predict using a requested model or all models if none specified
        model_map = {
            "lr": "logistic_regression",
            "rf": "random_forest",
            "dt": "decision_tree"
        }

        # If a specific model key was requested, return a simplified single-model response
        if requested_model:
            model_key = requested_model.lower()
            model_name = model_map.get(model_key)
            if not model_name:
                return jsonify({"error": f"Unknown model key '{requested_model}'. Use lr, rf or dt."}), 400

            res = predict_phishing(features, model_name=model_name)
            # normalize returned structure to what frontend expects
            return jsonify({
                "url": url,
                "model": model_name,
                "prediction": res.get("prediction"),
                "raw_label": res.get("raw_label"),
                "confidence": res.get("probability_phishing")
            })

        # Otherwise return results for all models (backwards compatible)
        results = []
        for key, model_name in model_map.items():
            res = predict_phishing(features, model_name=model_name)
            results.append({
                "model": model_name,
                "prediction": res.get("prediction"),
                "raw_label": res.get("raw_label"),
                "probability_phishing": res.get("probability_phishing")
            })

        return jsonify({
            "url": url,
            "results": results
        })

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

# ===========================
# 🚀 Run server
# ===========================
if __name__ == "__main__":
    # Run on 5000 so default frontend setups (http://127.0.0.1:5000) match
    app.run(host="0.0.0.0", port=5001, debug=True)
