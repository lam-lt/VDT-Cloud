from flask import Flask, jsonify, render_template
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient("mongodb://mongodb-server:27017/")
    mydb = client["students_db"]
    return mydb

@app.route("/")
def home():
    return "Hello from flask"

@app.route("/students")
def fetch_students():
    db = get_db()    
    all_user = db.names.find().sort("id")
    return render_template('index.html', users=all_user)

if __name__ == "__main__":
    app.run(debug=True)