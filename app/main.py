
from fastapi import FastAPI
import joblib
import os
import pandas as pd

app = FastAPI(title="Customer Churn Prediction API")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, "artifacts", "logistic_regression_model.pkl"))
pipeline = joblib.load(os.path.join(BASE_DIR, "artifacts", "logistic_regression_pipeline.pkl"))



@app.get("/")
def home():
    return {"message" : "Customer Churn Prediction API is running..."}


@app.post("/predict")
def predict(customer : dict):
    df = pd.DataFrame([customer])
    processed = pipeline.transform(df)
    prediction = model.predict(processed)[0]

    prediction_probability = model.predict_proba(processed)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": round(float(prediction_probability), 2)
    }