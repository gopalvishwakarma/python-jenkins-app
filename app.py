from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    country = request.form['country']
    password = request.form['password']

    # You can now save data to DB or process it
    print("Received Registration:")
    print(f"Name: {name}, Email: {email}, Gender: {gender}, Country: {country}, Password: {password}")

    return f"Thanks for registering, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
    serve(app, host='0.0.0.0', port=8000)
