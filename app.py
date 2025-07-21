from flask import Flask, render_template, request
from pymongo import MongoClient
from waitress import serve

app = Flask(__name__)

# Connect to MongoDB (local or Atlas)
client = MongoClient("mongodb://localhost:27017")  # for local
# client = MongoClient("mongodb+srv://<user>:<password>@cluster0.mongodb.net/")  # for Atlas


db = client["userdb"]
collection = db["users"]

@app.route('/')
def home():
    return render_template("register.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    collection.insert_one({'name': name, 'email': email})
    return "Registration Successful"

if __name__ == "__main__":
    # Run using waitress (production WSGI)
    serve(app, host='0.0.0.0', port=8000)
