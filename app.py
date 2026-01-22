from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def advert():
    return render_template("advert.html")

@app.route("/request", methods=["GET", "POST"])
def user_request():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO requests (name, message) VALUES (?, ?)",
            (name, message)
        )

        db.commit()
        db.close()

        return jsonify({"status": "success", "message": "Request saved successfully!"})

    return render_template("request.html")

@app.route("/store", methods=["GET", "POST"])
def store():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )
        db.commit()
        db.close()

        return jsonify({"status": "success", "message": "Data stored successfully!"})

    return render_template("store.html")

if __name__ == "__main__":
    app.run(debug=True)
