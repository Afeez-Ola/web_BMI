from flask import Flask, render_template, request
import os

os.getcwd()

app = Flask(__name__)

def getInputs():
    total_bill = float(input("What was the total bill: "))
    total_tip = float(input("What is the total tip: "))
    number_of_people = int(input("How many people to split with: "))


@app.route("/", methods=["GET", "POST"])
def main():
    result = None
    if request.method == "GET":
        result = "We are up"
    return result


if __name__ == "__main__":
    app.run()
