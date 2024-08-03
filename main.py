from flask import Flask, render_template, request
import os

os.getcwd()

app = Flask(__name__)

def calculateBMI(height,weight):
    bmi = weight / (height ** 2)
    return bmi



@app.route("/", methods=["GET", "POST"])
def main():
    result = None
    if request.method == "GET":
        result = "We are creating BMI calculator, In progress ..."
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()
