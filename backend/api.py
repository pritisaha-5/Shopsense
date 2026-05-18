from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load model (IMPORTANT: correct path from backend folder)
model = joblib.load("../models/churn_model.pkl")


@app.post("/predict")
def predict(data: dict):

    recency = data["recency"]
    frequency = data["frequency"]
    monetary = data["monetary"]

    features = np.array([[recency, frequency, monetary]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "churn": int(prediction),
        "probability": float(probability)
    }