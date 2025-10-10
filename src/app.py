from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import predict_phishing
from feature_extractor import extract_features_from_url

app = Flask(__name__)
CORS(app)

# ===========================
# 🔹 Home endpoint
# ===========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "🌐 Phishing Website Detection API",
        "usage": "Send POST request to /predict?model=lr|rf|dt with {'url': 'https://example.com'}",
        "example_request": {"url": "https://paypal-login-secure-update.com/account"},
        "example_response": {
            "model": "rf",
            "prediction": "Phishing",
            "raw_label": 1,
            "probability_phishing": 0.85,
            "url": "https://paypal-login-secure-update.com/account"
        }
    })

# ===========================
# 🔮 Predict endpoint
# ===========================
@app.route("/predict", methods=["POST"])
def predict():
    # 1️⃣ Get the model choice from query parameter
    model_choice = request.args.get("model", "rf").lower()
    model_map = {
        "lr": "logistic_regression",
        "rf": "random_forest",
        "dt": "decision_tree"
    }

    if model_choice not in model_map:
        return jsonify({"error": "Unknown model. Use model=lr, rf, or dt"}), 400

    model_name = model_map[model_choice]

    # 2️⃣ Get URL from JSON payload
    data = request.get_json(silent=True) or {}
    url = data.get("url")
    if not url:
        return jsonify({"error": "Missing 'url' field in JSON payload"}), 400

    try:
        # 3️⃣ Extract features from URL
        features = extract_features_from_url(url)

        # 4️⃣ Predict using selected model
        result = predict_phishing(features, model_name=model_name)

        # 5️⃣ Include original URL in response
        result["url"] = url

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


# ===========================
# 🚀 Run server
# ===========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
