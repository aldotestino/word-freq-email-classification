class EmailClassifier:
    def __init__(self, scaler, pca, model):
        self.scaler = scaler
        self.pca = pca
        self.model = model

    def predict(self, features):
        x = list(features.values())
        x = self.scaler.transform([x])
        x = self.pca.transform(x)
        pred = self.model.predict(x)
        return int(pred[0])
