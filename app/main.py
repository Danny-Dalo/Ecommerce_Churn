
from fastapi import FastAPI
import joblib
import os
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(title="Customer Churn Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, "artifacts", "logistic_regression_model.pkl"))
pipeline = joblib.load(os.path.join(BASE_DIR, "artifacts", "logistic_regression_pipeline.pkl"))



# @app.get("/")
# def home():

#     html_content = """
#     <html>
#       <head><title>Customer Churn Prediction API</title></head>
#       <body>
#         <h1>Customer Churn Prediction API is running...</h1>
#         <p> head to
#       </body>
#     </html>
#     """
#     return HTMLResponse(content=html_content)


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