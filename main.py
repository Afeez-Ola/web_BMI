from flask import Flask, render_template, request
import os

os.getcwd()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    result = None
    if request.method == "GET":
        result = "We are up"
    return result


if __name__ == "__main__":
    app.run()
