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
        "usage": "Send POST request to /predict with {'url': 'https://example.com'}",
        "example_request": {"url": "https://paypal-login-secure-update.com/account"},
        "example_response": {
            "model": "random_forest",
            "prediction": "Phishing",
            "raw_label": 1,
            "probability_phishing": 0.85
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

    try:
        # 1️⃣ Extract features from the URL
        features = extract_features_from_url(url)

        # 2️⃣ Predict using Random Forest by default
        result = predict_phishing(features, model_name="random_forest")

        # 3️⃣ Include original URL in response
        result["url"] = url

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


# ===========================
# 🚀 Run server
# ===========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
