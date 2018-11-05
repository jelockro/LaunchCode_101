from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import cgi
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:user@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(256))

    def __init__(self, title, body):
        self.title = title
        self.body = body


blogs = []

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_title = request.form['title']
        blog_body = request.form['body']
        new_blog = Blog(blog_title, blog_body)
        db.session.add(new_blog)
        db.session.commit()
        return render_template('blogs.html',title="Build a Blog!")
    else:
        return render_template('blog_form.html', title="Buld a Blog!")

@app.route('/blogs', methods=['POST', 'GET'])
def blogs():
    blogs = Blog.query.all()
    return render_template('blogs.html',title="Build a Blog!", blogs=blogs)

if __name__ == "__main__":
    app.run()