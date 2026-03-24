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

import os

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
