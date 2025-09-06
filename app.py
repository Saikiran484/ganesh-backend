from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"expenses": [], "members": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/expenses", methods=["GET", "POST"])
def expenses():
    data = load_data()
    if request.method == "POST":
        new_expense = request.json
        data["expenses"].append(new_expense)
        save_data(data)
        return jsonify({"message": "Expense added"}), 201
    return jsonify(data["expenses"])

@app.route("/members", methods=["GET", "POST"])
def members():
    data = load_data()
    if request.method == "POST":
        new_member = request.json
        data["members"].append(new_member)
        save_data(data)
        return jsonify({"message": "Member added"}), 201
    return jsonify(data["members"])

if __name__ == "__main__":
    app.run(debug=True)
