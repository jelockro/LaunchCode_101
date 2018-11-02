from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import cgi
import os

import jinja2
app =Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://get-it-done:user@localhost:8889/get-it-done'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('todos.html', title="Get It Done", tasks=tasks)

if __name__ == "__main__":
    app.run()