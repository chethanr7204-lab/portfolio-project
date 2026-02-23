from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, email TEXT)")
    cursor.execute("INSERT INTO contacts (name, email) VALUES (?, ?)", (name, email))

    conn.commit()
    conn.close()

    return "Data Saved Successfully!"

if __name__ == '__main__':
    app.run(debug=True)