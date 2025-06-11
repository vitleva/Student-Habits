import joblib
import json

# Загружаем модель один раз при импорте
model = joblib.load("model.joblib")

def predict_score(features):
    return model.predict([features])[0]

def evaluate_model():
    """Загружает метрики из файла и возвращает их"""
    with open("metrics.json", "r") as f:
        metrics = json.load(f)
    return metrics["r2"], metrics["mae"], metrics["mse"]






