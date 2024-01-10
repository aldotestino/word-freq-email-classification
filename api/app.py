import os
from pydantic import BaseModel
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from sklearn.linear_model import LogisticRegression
import uvicorn
from sklearn.preprocessing import StandardScaler
import joblib

from email_classifier import EmailClassifier

sc: StandardScaler = joblib.load('saved_scaler.joblib')
model: LogisticRegression = joblib.load('saved_model.joblib')
ec = EmailClassifier(model, sc)

PORT = int(os.environ.get("PORT", 8000))

app = FastAPI()

origins = [
  "*"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

class Data(BaseModel):
  text: str


@app.post('/predict', status_code=status.HTTP_200_OK)
def predict(data: Data):
  return {
    'text': data.text,
    'prediction': ec.predict(data.text)
  }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=PORT)


### TEST EMAIL
"""
Subject: 🌟 UNMISSABLE OPPORTUNITY - ACT NOW! 🌟

Dear [Your Name],

Seize the chance for a business transformation! REMOVE barriers, ORDER now, and SURF the internet of success with our cutting-edge solutions.

MAIL us to RECEIVE a special offer, and FREE yourself from the ordinary. Don't miss out - YOUR success is our mission!

Act FAST - call 857-415-85 for a direct line to SUCCESS. Let DATA drive your decisions; we're the TECHNOLOGY revolution!

MONEY BACK GUARANTEE - this offer is LIMITED. Don't let it slip away; be the 85th person to join our success story.

Best,
"""