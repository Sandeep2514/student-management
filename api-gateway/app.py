from flask import Flask, jsonify
import requests

app = Flask(__name__)

STUDENT_SERVICE = "http://localhost:5000"
COURSE_SERVICE = "http://localhost:5001"
RESULT_SERVICE = "http://localhost:5002"


@app.route("/")
def home():
    return "API Gateway Running Successfully"


@app.route("/students")
def students():

    response = requests.get(f"{STUDENT_SERVICE}/students")

    return jsonify(response.json())


@app.route("/courses")
def courses():

    response = requests.get(f"{COURSE_SERVICE}/courses")

    return jsonify(response.json())


@app.route("/results")
def results():

    response = requests.get(f"{RESULT_SERVICE}/results")

    return jsonify(response.json())


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000, debug=True)
