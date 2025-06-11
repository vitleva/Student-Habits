from flask import Flask, render_template, request
from models import *
from utils import preprocess_input
from ml_model import predict_score, evaluate_model

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = request.form
        # Сохраняем данные в базу
        student_id = form_data['student_id']
        insert_student(student_id, form_data['age'], form_data['gender'], form_data['parental_education_level'])
        insert_lifestyle(
            student_id,
            form_data['sleep_hours'],
            form_data['exercise_frequency'],
            form_data['social_media_hours'],
            form_data['netflix_hours'],
            True if form_data['part_time_job'] == "Да" else False,
            form_data['diet_quality'],
            form_data['internet_quality'],
            form_data['mental_health_rating'],
            True if form_data['extracurricular_participation'] == "Да" else False
        )
        insert_attendance(student_id, form_data['attendance_percentage'])
        features = preprocess_input(form_data)
        predicted_score = predict_score(features)
        save_prediction(student_id, predicted_score)
        r2, mae, mse = evaluate_model()
        return render_template("result.html", 
                                prediction=round(predicted_score, 2),
                                form_data=form_data,
                                r2=round(r2, 2), mae=round(mae,2), mse=round(mse,2)
                                )


    return render_template("form.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form
        features = preprocess_input(data)
        prediction = predict_score(features)
        r2, mae, mse = evaluate_model()
        return render_template("result.html", prediction=prediction, r2=round(r2, 2), mae=round(mae,2), mse=round(mse,2))
    except Exception as e:
        return render_template("error.html", error=str(e))

@app.route("/history", methods=["GET", "POST"])
def history():
    min_score = request.form.get("min_score")
    max_score = request.form.get("max_score")

    if min_score and max_score:
        raw_history = get_prediction_history(float(min_score), float(max_score))
    else:
        raw_history = get_prediction_history()

    # Создаём новый список с преобразованным значением предсказания
    history = []
    for row in raw_history:
        try:
            new_row = list(row)  # превращаем кортеж в список
            new_row[0] = new_row[0]
            new_row[1] = new_row[1]
            new_row[2] = float(new_row[2])
            new_row[3] = new_row[3]
            history.append(new_row)
        except (ValueError, IndexError):
            continue  

    return render_template("history.html", history=history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))





