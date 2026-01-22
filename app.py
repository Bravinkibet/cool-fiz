from flask import Flask, render_template, request
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
        return f"Request received from {name}"
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

        return "Data stored successfully!"
    return render_template("store.html")


if __name__ == "__main__":
    print("Flask server starting...")
    app.run(debug=True)
