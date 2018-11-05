from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config
import cgi
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

blogs = []

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog = request.form['blog']
        blogs.append(blog)

    return render_template('blogs.html',title="Build a Blog!", blogs=blogs)


app.run()