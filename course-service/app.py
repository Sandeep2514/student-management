from flask import Flask, jsonify, request

app = Flask(__name__)

courses = [
    {
        "id": 1,
        "name": "Python",
        "duration": "3 Months"
    },
    {
        "id": 2,
        "name": "DevOps",
        "duration": "6 Months"
    }
]

@app.route("/")
def home():
    return "Course Service Running Successfully"

@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify(courses)

@app.route("/courses", methods=["POST"])
def add_course():

    course = request.get_json()

    courses.append(course)

    return jsonify({
        "message":"Course Added Successfully",
        "course":course
    }),201

@app.route("/courses/<int:id>", methods=["GET"])
def get_course(id):

    for course in courses:

        if course["id"] == id:

            return jsonify(course)

    return jsonify({
        "message":"Course Not Found"
    }),404


@app.route("/courses/<int:id>", methods=["PUT"])
def update_course(id):

    data = request.get_json()

    for course in courses:

        if course["id"] == id:

            course["name"] = data["name"]
            course["duration"] = data["duration"]

            return jsonify({
                "message":"Course Updated Successfully",
                "course":course
            })

    return jsonify({
        "message":"Course Not Found"
    }),404


@app.route("/courses/<int:id>", methods=["DELETE"])
def delete_course(id):

    for course in courses:

        if course["id"] == id:

            courses.remove(course)

            return jsonify({
                "message":"Course Deleted Successfully"
            })

    return jsonify({
        "message":"Course Not Found"
    }),404


if __name__=="__main__":

    app.run(host="0.0.0.0",port=5001,debug=True)
