import joblib
import json
import os

# Загружаем модель один раз при импорте
# Получаем абсолютный путь к текущей папке (где находится ml_model.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Собираем путь к файлу модели
model_path = os.path.join(BASE_DIR, "model.joblib")

# Загружаем модель с помощью joblib
model = joblib.load(model_path)

# Путь к файлу метрик
metrics_path = os.path.join(BASE_DIR, "..", "metrics.json")

def predict_score(features):
    return model.predict([features])[0]

def evaluate_model():
    """Загружает метрики из файла и возвращает их"""
    with open(metrics_path, "r") as f:
        metrics = json.load(f)
    return metrics["r2"], metrics["mae"], metrics["mse"]






