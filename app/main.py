
from fastapi import FastAPI
import joblib
import pandas as pd
from typing import Union

app = FastAPI(title="Customer Churn Prediction API")

model = joblib.load("../artifacts/logistic_regression_model.pkl")

pipeline = joblib.load("../artifacts/logistic_regression_pipeline.pkl")

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