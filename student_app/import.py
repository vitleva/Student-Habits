import pandas as pd
import sqlite3

# Подключение к БД
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Загрузка данных из CSV
df = pd.read_csv("student_app/uploads/students.csv")

for _, row in df.iterrows():
    # === 1. Вставка в таблицу Student ===
    cursor.execute("""
        INSERT OR IGNORE INTO Student (id, age, gender, parental_education_level)
        VALUES (?, ?, ?, ?)
    """, (
        row["student_id"],
        row["age"],
        row["gender"],
        row["parental_education_level"]
    ))

    # === 2. Вставка в таблицу Lifestyle ===
    cursor.execute("""
        INSERT INTO Lifestyle (student_id, sleep_hours, exercise_frequency, social_media_hours,
                               netflix_hours, part_time_job, diet_id, internet_id,
                               mental_health_rating, extracurricular_participation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row["student_id"],
        row["sleep_hours"],
        row["exercise_frequency"],
        row["social_media_hours"],
        row["netflix_hours"],
        row["part_time_job"],
        row["diet_quality"],        
        row["internet_quality"],    
        row["mental_health_rating"],
        row["extracurricular_participation"]
    ))

    # === 3. Вставка в таблицу Attendance ===
    cursor.execute("""
        INSERT INTO Attendance (student_id, attendance_percentage)
        VALUES (?, ?)
    """, (
        row["student_id"],
        row["attendance_percentage"]
    ))

# Завершаем транзакцию
conn.commit()
cursor.close()
conn.close()
