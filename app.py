from flask import Flask, jsonify, request ,render_template
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pachipala@13300k",
        database="book_shop"
    )


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student", methods=["GET"])
def get_students():
    db = get_db_connection()
    mc = db.cursor(dictionary=True)

    mc.execute("SELECT * FROM stud")
    r = mc.fetchall()

    mc.close()
    db.close()

    return jsonify(r)

@app.route("/student/<int:id>", methods=["GET"])
def get_student(id):
    db = get_db_connection()
    mc = db.cursor(dictionary=True)

    mc.execute("SELECT * FROM stud WHERE sno=%s", (id,))
    r = mc.fetchone()

    mc.close()
    db.close()

    return jsonify(r)

@app.route("/student", methods=["POST"])
def add_student():
    data = request.json

    db = get_db_connection()
    mc = db.cursor()

    if isinstance(data, list):
        for student in data:
            mc.execute(
                "INSERT INTO stud (sno, name, age, mobile) VALUES (%s, %s, %s, %s)",
                (
                    student["sno"],
                    student["name"],
                    student["age"],
                    student["mobile"]
                )
            )
    else:
        mc.execute(
            "INSERT INTO stud (sno, name, age, mobile) VALUES (%s, %s, %s, %s)",
            (
                data["sno"],
                data["name"],
                data["age"],
                data["mobile"]
            )
        )

    db.commit()

    mc.close()
    db.close()

    return jsonify({"message": "Student(s) added successfully"})

if __name__ == "__main__":
    app.run(debug=True)