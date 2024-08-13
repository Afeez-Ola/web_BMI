from flask import Flask, render_template, request
import os

os.getcwd()

app = Flask(__name__)


# def getInputs():
#     bill_amount = float(input("What was the total bill: "))
#     tip_percentage = float(input("What is the total tip: "))
#     number_of_people = int(input("How many people to split with: "))
#
#     return tip_percentage, bill_amount, number_of_people


def tip_calculations(tip_percentage, bill_amount, number_of_people):
    total_tip = bill_amount * (float(tip_percentage) / 100)
    total_bill = float(total_tip + bill_amount)
    amount_per_person = float(total_bill / number_of_people)
    return total_bill, total_tip, amount_per_person


@app.route("/", methods=["GET", "POST"])
def main():
    total_bill, total_tip, amount_per_person = None, None, None
    if request.method == "POST":
        bill_amount = request.form["bill-amount"]
        tip_percentage = request.form["tip-percentage"]
        number_of_people = request.form["number-of-people"]

        total_bill, total_tip, amount_per_person = tip_calculations(tip_percentage, bill_amount, number_of_people)

    return render_template("index.html", total_bill=total_bill, total_tip=total_tip,
                           amount_per_person=amount_per_person)


if __name__ == "__main__":
    app.run()
