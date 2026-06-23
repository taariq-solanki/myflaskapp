from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(os.environ["DATABASE_URL"])

@app.route("/")
def home():
    return "Hello bachhhhho from Docker! 🐳"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/users")
def get_users():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route("/users/add")
def add_user():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES ('Taariq') RETURNING *;")
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "User added!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)