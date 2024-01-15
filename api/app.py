import os
from pydantic import BaseModel
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
import joblib
from model.feature_extractor1 import FeatureExtractor1
from model.feature_extractor2 import FeatureExtractor2
from constants import words1, words2, chars1
from model.email_classifier import EmailClassifier

sc_1: StandardScaler = joblib.load('./model/saved/scaler_1.joblib')
pca_1: PCA = joblib.load('./model/saved/best_pca_1.joblib')
model_1: SGDClassifier = joblib.load('./model/saved/best_model_1.joblib')
ec1 = EmailClassifier(scaler=sc_1, pca=pca_1, model=model_1)

sc_2: StandardScaler = joblib.load('./model/saved/scaler_2.joblib')
pca_2: PCA = joblib.load('./model/saved/best_pca_2.joblib')
model_2: SGDClassifier = joblib.load('./model/saved/best_model_2.joblib')
ec2 = EmailClassifier(scaler=sc_2, pca=pca_2, model=model_2)

fe1 = FeatureExtractor1(words=words1, chars=chars1)
fe2 = FeatureExtractor2(words=words2)

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
  model: str
  text: str


@app.get('/')
def healthcheck():
  return {'status': 'ok'}


@app.post('/predict', status_code=status.HTTP_200_OK)
def predict(data: Data):
  if(data.model == "1"):
     features = fe1.extract_features(data.text)
     return {
      'text': data.text,
      'prediction': ec1.predict(features=features)
    }
  else:
    features = fe2.extract_features(data.text)
    return {
      'text': data.text,
      'prediction': ec2.predict(features=features)
    }


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=PORT)
