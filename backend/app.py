from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "users.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)


@app.route("/")
def health():
    return {
        "status": "Backend Running"
    }


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")

    with open(DATA_FILE, "r") as f:
        users = json.load(f)

    users.append({
        "name": name,
        "email": email
    })

    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

    return jsonify({
        "message": "Registration Successful",
        "user": {
            "name": name,
            "email": email
        }
    })


@app.route("/users")
def users():

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return jsonify(data)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000
    )