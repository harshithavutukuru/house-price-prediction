from flask import Flask, request, jsonify, render_template
from src.predict import predict_price

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = data["features"]  # single value in a list
    price = predict_price(features)
    return jsonify({"predicted_price": price})

if __name__ == "__main__":
    app.run(debug=True)
