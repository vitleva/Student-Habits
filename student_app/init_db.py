import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()

# Таблица Student
c.execute('''
CREATE TABLE IF NOT EXISTS Student (
    id TEXT PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    parental_education_level TEXT
);
''')

# Таблица Lifestyle
c.execute('''
CREATE TABLE IF NOT EXISTS Lifestyle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT UNIQUE,
    sleep_hours REAL,
    exercise_frequency INTEGER,
    social_media_hours REAL,
    netflix_hours REAL,
    part_time_job BOOLEAN,
    diet_id TEXT,
    internet_id TEXT,
    mental_health_rating INTEGER,
    extracurricular_participation BOOLEAN,
    FOREIGN KEY(student_id) REFERENCES Student(id)
);
''')

# Таблица Attendance
c.execute('''
CREATE TABLE IF NOT EXISTS Attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT UNIQUE,
    attendance_percentage REAL,
    FOREIGN KEY(student_id) REFERENCES Student(id)
);
''')

# Таблица Prediction
c.execute('''
CREATE TABLE IF NOT EXISTS Prediction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT UNIQUE,
    exam_score REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(student_id) REFERENCES Student(id)
);
''')

conn.commit()
conn.close()
