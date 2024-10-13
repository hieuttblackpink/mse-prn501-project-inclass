from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/path")
def path():
    print(request.args)
    return "Hi"

@app.route("/churn_count")
def churn_count():
    data = pd.read_csv("/Users/hieutt/MSE - FPT/Fall 2024/PPR501/Project/In-class/Day5/RestfulAPI/Telco-Customer-Churn.csv")
    result = data["Churn"].to_json()
    return result

@app.route("/3-body")
def three_body():
    file = open("/Users/hieutt/MSE - FPT/Fall 2024/PPR501/Project/In-class/Day5/RestfulAPI/file.txt", 'r', encoding = 'utf-8')
    data = file.read()
    return data

# @app.route("/login")

if __name__ == "__main__":
    app.run()