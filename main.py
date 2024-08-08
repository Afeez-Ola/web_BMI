from flask import Flask, render_template, request
import os

os.getcwd()

app = Flask(__name__)


def getInputs():
    bill_amount = float(input("What was the total bill: "))
    tip_percentage = float(input("What is the total tip: "))
    number_of_people = int(input("How many people to split with: "))

    return tip_percentage,bill_amount,number_of_people

def tip_calculations():
    tip_percentage, bill_amount, number_of_people = getInputs()

    total_tip = bill_amount * (tip_percentage / 100)
    total_bill = total_tip + bill_amount
    return total_bill

@app.route("/", methods=["GET", "POST"])
def main():
    result = None
    if request.method == "GET":
        result = "We are up"
    return result


if __name__ == "__main__":
    app.run()
