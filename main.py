# We are creating BMI calculator now
from flask import Flask, render_template, request

import os

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'))


def bmi_calculations(height, weight):
    bmi_result = int(weight / (height ** 2))
    return bmi_result


def bmi_interpreter(bmi):
    if bmi < 18.5:
        interpretation = "You are underweight"
    elif bmi < 25:
        interpretation = "You have Normal Weight"
    elif bmi < 30:
        interpretation = "You are Overweight"
    else:
        interpretation = "You are obese"
    return interpretation


@app.route("/", methods=["GET", "POST"])
def getUserInfo():
    result = None
    if request.method == "POST":
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])

            if height <= 0 or weight <= 0:
                raise ValueError("Invalid, please enter a positive number")

            bmi_result = bmi_calculations(height, weight)
            result = {
                'bmi': int(bmi_result),
                'category': bmi_interpreter(bmi_result)
            }

        except ValueError as e:
            result = {'error': str(e)}
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
