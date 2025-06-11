def preprocess_input(data):
    # Категориальные словари
    gender_map = {"Male": 0, "Female": 1, "Мужской": 0, "Женский": 1}
    diet_quality_map = {
        "Poor": 0, "Fair": 1, "Good": 2,
        "Плохое": 0, "Удовлетворительное": 1, "Хорошее": 2
    }
    yes_no_map = {"Yes": 1, "No": 0, "Да": 1, "Нет": 0}

    try:
        gender = gender_map.get(data['gender'], -1)
        diet_quality = diet_quality_map.get(data['diet_quality'], -1)
        part_time_job = yes_no_map.get(data['part_time_job'], -1)
        extracurricular = yes_no_map.get(data['extracurricular_participation'], -1)

        if -1 in [gender, diet_quality, part_time_job, extracurricular]:
            raise ValueError("Некорректные значения в одном из категориальных полей.")

        features = [
            float(data['study_hours_per_day']),
            float(data['sleep_hours']),
            int(data['exercise_frequency']),
            float(data['social_media_hours']),
            float(data['netflix_hours']),
            part_time_job,
            float(data['mental_health_rating']),
            extracurricular,
            float(data['attendance_percentage']),
        ]
        return features

    except Exception as e:
        raise ValueError(f"Ошибка обработки данных: {e}")





