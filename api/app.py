import os
from pydantic import BaseModel
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
import joblib

from model.email_classifier import EmailClassifier

sc: StandardScaler = joblib.load('./model/scaler.joblib')
pca: PCA = joblib.load('./model/best_pca.joblib')
model: LogisticRegression = joblib.load('./model/best_model.joblib')
ec = EmailClassifier(scaler=sc, pca=pca, model=model)

PORT = int(os.environ.get("PORT", 8080))

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

@app.get('/')
def healthcheck():
  return {'status': 'ok'}


@app.post('/predict', status_code=status.HTTP_200_OK)
def predict(data: Data):
  return {
    'text': data.text,
    'prediction': ec.predict(data.text)
  }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=PORT)
