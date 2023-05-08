from fastapi import FastAPI
import numpy as np
import pandas as pd
from uvicorn import run
import os
from setfit import SetFitClassifier
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from setfit import SetFitClassifier


app = FastAPI()
model_dir = 'saved_model'
model = SetFitClassifier.load(model_dir)


origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def welcome():
    return Response("Welcome to Orbitshift API!! Please provide a Job Title to get its Job Class...")

@app.post('/predict')
async def predict_job_class(job_title: str):
    if job_title == "":
        Response("No Job Title provided")
    df = pd.DataFrame()
    df['job_title'] = [str(job_title)]
    job_title = df['job_title'].to_list()
    prediction = model.predict(job_title)
    predicted_job_class = prediction[0]
    return f"Class {predicted_job_class}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    run(app, host="0.0.0.0", port=port)