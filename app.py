from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model_path = "best_model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file '{model_path}' not found. Please upload it.")

model = joblib.load(model_path)

# Mapping for ocean_proximity categories (Ensure this matches training data)
ocean_proximity_mapping = {
    "NEAR BAY": 0,
    "<1H OCEAN": 1,
    "INLAND": 2,
    "NEAR OCEAN": 3,
    "ISLAND": 4
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json.get("features", [])  # Get input features from request
        if not data or not isinstance(data, list):
            return jsonify({"error": "Invalid input format. Expected a list of feature values."}), 400

        # Extract ocean_proximity (last value in features list)
        ocean_proximity_label = data.pop()  # Get last item (ocean proximity)
        ocean_proximity_encoded = ocean_proximity_mapping.get(ocean_proximity_label, -1)  # Encode it

        if ocean_proximity_encoded == -1:
            return jsonify({"error": "Invalid ocean_proximity value."}), 400

        # Append encoded ocean_proximity back into the features list
        features = np.array(data + [ocean_proximity_encoded]).reshape(1, -1)

        # Predict
        prediction = model.predict(features)[0]

        return jsonify({"predicted_price": round(float(prediction), 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render assigns a dynamic port
    app.run(debug=True, host="0.0.0.0", port=port)  # Ensure it runs on all interfaces
