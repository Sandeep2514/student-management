from flask import Flask, jsonify, request

app = Flask(__name__)

results = [
    {
        "student_id": 1,
        "course_id": 1,
        "marks": 95,
        "grade": "A"
    },
    {
        "student_id": 2,
        "course_id": 2,
        "marks": 82,
        "grade": "B"
    }
]

@app.route("/")
def home():
    return "Result Service Running Successfully"


@app.route("/results", methods=["GET"])
def get_results():
    return jsonify(results)


@app.route("/results", methods=["POST"])
def add_result():

    result = request.get_json()

    results.append(result)

    return jsonify({
        "message": "Result Added Successfully",
        "result": result
    }), 201


@app.route("/results/<int:student_id>", methods=["GET"])
def get_result(student_id):

    for result in results:

        if result["student_id"] == student_id:
            return jsonify(result)

    return jsonify({
        "message": "Result Not Found"
    }), 404


@app.route("/results/<int:student_id>", methods=["PUT"])
def update_result(student_id):

    data = request.get_json()

    for result in results:

        if result["student_id"] == student_id:

            result["course_id"] = data["course_id"]
            result["marks"] = data["marks"]
            result["grade"] = data["grade"]

            return jsonify({
                "message": "Result Updated Successfully",
                "result": result
            })

    return jsonify({
        "message": "Result Not Found"
    }), 404


@app.route("/results/<int:student_id>", methods=["DELETE"])
def delete_result(student_id):

    for result in results:

        if result["student_id"] == student_id:

            results.remove(result)

            return jsonify({
                "message": "Result Deleted Successfully"
            })

    return jsonify({
        "message": "Result Not Found"
    }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
