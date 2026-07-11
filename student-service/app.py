from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Sandeep",
        "department": "CSE"
    },
    {
        "id": 2,
        "name": "Rahul",
        "department": "ECE"
    }
]

@app.route("/")
def home():
    return "Student Service Running Successfully"

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.get_json()

    for student in students:

        if student["id"] == id:

            student["name"] = data["name"]
            student["department"] = data["department"]

            return jsonify({
                "message": "Student Updated Successfully",
                "student": student
            })

    return jsonify({
        "message": "Student Not Found"
    }), 404

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):

    for student in students:

        if student["id"] == id:

            return jsonify(student)

    return jsonify({
        "message":"Student Not Found"
    }),404

@app.route("/students", methods=["POST"])
def add_student():

    student = request.get_json()

    students.append(student)

    return jsonify({
        "message": "Student Added Successfully",
        "student": student
    }), 201

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    for student in students:

        if student["id"] == id:

            students.remove(student)

            return jsonify({
                "message": "Student Deleted Successfully"
            })

    return jsonify({
        "message": "Student Not Found"
    }),404    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
