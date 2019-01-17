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

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(256))

    def __init__(self, title, body):
        self.title = title
        self.body = body


blogs = []

@app.route('/newpost', methods=['POST', 'GET'])
def index():
    title_error = ''    
    body_error = ''
    errors = []
    if request.method == 'POST':
        post_title = cgi.escape(request.form['title'])
        if post_title == '':
            title_error = "Please fill in the title"
            errors.append(title_error)
        
        post_body = cgi.escape(request.form['body'])
        if post_body == '':
            body_error = "Please fill in the body"
            errors.append(body_error)
        
        if errors:
            return render_template("blog_form.html", title=post_title, body=post_body, title_error=title_error, body_error=body_error )
        
        new_post = Post(post_title, post_body)
        db.session.add(new_post)
        db.session.commit()
        post_id = new_post.id
        return redirect('/post?post_id=' + str(post_id))
    else:
        return render_template('blog_form.html')

@app.route('/', methods=['POST', 'GET'])
@app.route('/blog', methods=['POST', 'GET'])
def blog():
    posts = Post.query.all()
    
    if request.args:
        print('request.args: ', request.args)
        post_id = request.args.get("post_id")
        print('post_id: ', post_id)
        return redirect('/post?post_id=' + post_id)


    return render_template('blog.html', posts=posts)

@app.route('/post')
def post():
    post_id = request.args.get("post_id")
    post = Post.query.get(post_id)
    
    return render_template('post_template.html', post=post)


if __name__ == "__main__":
    app.run()