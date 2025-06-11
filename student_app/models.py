import sqlite3

def get_connection():
    return sqlite3.connect("students.db")


def insert_student(student_id, age, gender, parental_education_level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT OR IGNORE INTO Student (id, age, gender, parental_education_level)
        VALUES (?, ?, ?, ?)
    """, (student_id, age, gender, parental_education_level))
    conn.commit()
    cur.close()
    conn.close()


def insert_lifestyle(student_id, sleep_hours, exercise_frequency, social_media_hours,
                     netflix_hours, part_time_job, diet_id, internet_id,
                     mental_health_rating, extracurricular_participation):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Lifestyle (
            student_id, sleep_hours, exercise_frequency, social_media_hours,
            netflix_hours, part_time_job, diet_id, internet_id,
            mental_health_rating, extracurricular_participation
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(student_id) DO UPDATE SET
            sleep_hours = excluded.sleep_hours,
            exercise_frequency = excluded.exercise_frequency,
            social_media_hours = excluded.social_media_hours,
            netflix_hours = excluded.netflix_hours,
            part_time_job = excluded.part_time_job,
            diet_id = excluded.diet_id,
            internet_id = excluded.internet_id,
            mental_health_rating = excluded.mental_health_rating,
            extracurricular_participation = excluded.extracurricular_participation;
    """, (student_id, sleep_hours, exercise_frequency, social_media_hours,
          netflix_hours, part_time_job, diet_id, internet_id,
          mental_health_rating, extracurricular_participation))
    conn.commit()
    cur.close()
    conn.close()


def insert_attendance(student_id, attendance_percentage):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Attendance (student_id, attendance_percentage)
        VALUES (?, ?)
        ON CONFLICT(student_id) DO UPDATE SET
            attendance_percentage = excluded.attendance_percentage;
    """, (student_id, attendance_percentage))
    conn.commit()
    cur.close()
    conn.close()


def save_prediction(student_id, predicted_score):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT OR REPLACE INTO Prediction (student_id, exam_score)
        VALUES (?, ?)
    """, (student_id, predicted_score))
    conn.commit()
    cur.close()
    conn.close()


def get_prediction_history(min_score=None, max_score=None):
    conn = get_connection()
    cur = conn.cursor()
    if min_score is not None and max_score is not None:
        cur.execute("""
            SELECT * FROM Prediction
            WHERE exam_score BETWEEN ? AND ?
        """, (min_score, max_score))
    else:
        cur.execute("SELECT * FROM Prediction")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
