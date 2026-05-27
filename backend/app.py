
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("trips.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS trips(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        budget TEXT
    )""")
    conn.commit()
    conn.close()

@app.route("/save", methods=["POST"])
def save():
    data = request.json
    conn = sqlite3.connect("trips.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trips (name, category, budget) VALUES (?, ?, ?)",
                   (data["name"], data["category"], data["budget"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Saved"})

@app.route("/get", methods=["GET"])
def get():
    conn = sqlite3.connect("trips.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trips")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
