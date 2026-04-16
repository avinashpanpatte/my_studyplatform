from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# ✅ Create instance folder and DB path
instance_path = os.path.join(os.path.dirname(__file__), 'instance')
os.makedirs(instance_path, exist_ok=True)
db_path = os.path.join(instance_path, 'users.db')

# ✅ Create DB
def init_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ✅ REGISTER
@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password required"}), 400

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE username=?", (username,))
        if c.fetchone():
            conn.close()
            return jsonify({"message": "User already exists"}), 400

        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()

        user_id = c.lastrowid
        conn.close()

        print(f"🆕 New User Registered: ID={user_id}, Username={username}")

        return jsonify({"message": "success"}), 201
    except Exception as e:
        print(f"❌ Signup Error: {str(e)}")
        return jsonify({"message": f"Error: {str(e)}"}), 500

# ✅ LOGIN
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password required"}), 400

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute("SELECT id, username FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            print(f"✅ User Login: ID={user[0]}, Username={user[1]}")
            return jsonify({"message": "success"}), 200
        else:
            print(f"❌ Failed login: {username}")
            return jsonify({"message": "Invalid login"}), 401
    except Exception as e:
        print(f"❌ Login Error: {str(e)}")
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    print("✅ Database initialized at:", db_path)
    app.run(debug=True, host="127.0.0.1", port=5000)