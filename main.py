from flask import Flask, render_template, request
import os

os.getcwd()

app = Flask(__name__)


def calculateBMI(height, weight):
    bmi = weight / (height ** 2)
    return bmi


def bmi_categories(bmi):
    if bmi < 18.5:
        category = "You are underweight"
    elif bmi < 24:
        category = "You are Normal Weight"
    elif bmi < 30:
        category = "You are Over weight"
    else:
        category = "You are Obese"
    return category


@app.route("/", methods=["GET", "POST"])
def main():
    result = None
    try:
        if request.method == "POST":
            height = float(request.form["height"])
            weight = float(request.form["weight"])
            bmi = int(calculateBMI(height, weight))
            category = bmi_categories(bmi)
            result = {
                "bmi": bmi,
                "category": category
            }
            print(result)
    except ValueError as error:
        result = {"error": str(error)}
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()
