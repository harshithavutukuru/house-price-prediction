import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "linear_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "..", "models", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_price(features: list):
    X = np.array(features).reshape(1, -1)
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)
    return float(prediction[0])
