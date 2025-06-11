import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import json

# Загрузка данных 
df = pd.read_csv("students.csv")  

# Преобразование категориальных признаков 
df["part_time_job"] = df["part_time_job"].map({"Yes": 1, "No": 0})
df["extracurricular_participation"] = df["extracurricular_participation"].map({"Yes": 1, "No": 0})
df["diet_id"] = df["diet_quality"].map({"Poor": 0, "Fair": 1, "Good": 2})
df["internet_id"] = df["internet_quality"].map({"Poor": 0, "Average": 1, "Good": 2})

df["gender"] = df["gender"].map({"Male": 0, "Female": 1})
df["parental_education_level"] = df["parental_education_level"].map({"High School": 0, "Bachelor": 1, "Master": 2})


# Формируем X и y 
X = df[[
    "study_hours_per_day",
    "sleep_hours", "exercise_frequency", "social_media_hours",
    "netflix_hours", "part_time_job", "mental_health_rating",
    "extracurricular_participation", "attendance_percentage"
]]

y = df["exam_score"]

# Делим выборку
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Обучаем модель 
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)



# Оценка
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"R² = {r2:.2f}")
print(f"MAE = {mae:.2f}")
print(f"MSE = {mse:.2f}")


# Сохраняем модель 
joblib.dump(model, "model.joblib")

# Сохраняем метрики в JSON
metrics = {
    "r2": r2,
    "mae": mae,
    "mse": mse
}
with open("metrics.json", "w") as f:
    json.dump(metrics, f)

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- FEATURE IMPORTANCE ---
importances = model.feature_importances_
features = X.columns
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
sns.barplot(x=importances[indices], y=features[indices])
plt.title("Важность признаков (Feature Importance)")
plt.tight_layout()
plt.show()


# --- PREDICTED vs ACTUAL ---
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel("Истинное значение")
plt.ylabel("Прогноз модели")
plt.title("Прогноз vs Истинное значение")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.tight_layout()
plt.show()



