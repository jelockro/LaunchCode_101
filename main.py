from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
import cgi
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:user@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(256))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, body, owner):
        self.title = title
        self.body = body
        self.owner = owner

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))
    posts = db.relationship('Post', backref='owner') 

    def __init__(self, username, password):
        self.username = username
        self.password = password

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

@app.route('/login', methods=['POST', 'GET'])
def login():
    username_error = ''    
    password_error = ''
    database_error = ''
    errors = []
    if request.method == 'POST':
        esc_username = cgi.escape(request.form['username'])
        print('esc_username:', esc_username)
        if esc_username == '':
            username_error = "Username cannot be left blank"
            errors.append(username_error)
        
        
        esc_password = cgi.escape(request.form['password'])
        if esc_password == '':
            password_error = "Password cannot be left blank"
            errors.append(password_error)
        user = User.query.filter_by(username=esc_username).first()
        print('user: ', user)
        if user:
            print('if user passed on none')
        if user and user.password == pasword:
            print('is it really a success?')
            return render_template('success.html')
        if not user:
            database_error = 'User is not in database. Please Register.'
            errors.append(database_error)
        print('errors: ', errors)
        if errors:
            return render_template("login.html", username=esc_username, database_error=database_error, username_error=username_error, password_error=password_error )
        
        return render_template("success.html")
    else:
        return render_template('login.html')
@app.route('/', methods=['POST', 'GET'])
@app.route('/signup')
def signup():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['Password']
        
        email = request.form['Email (optional)']
        verify = request.form['Verify Password']
        errors =[]
        print('password:', password)
        print('verfiy:', verify)
        print('email:', email)
        redirectString='/?'
        if username == '':
            usernameError = "Username Cannot be Left Blank"
            errors.append('usernameError=' + usernameError)
        if len(username) < 3 :
            usernameError = "Username Must be Longer Than 3 Characters"
            errors.append('usernameError=' + usernameError)
        if len(username) > 20 :
            usernameError = "Username Must Be Shorter than 20 Characters"
            errors.append('usernameError=' + usernameError)
        if password == '':
            passwordError = "passwordError=Password Cannot Be Left Blank"
            errors.append(passwordError)
        if password != verify:
            verifyError = "Passwords Do Not Match"
            errors.append('verifyError=' + verifyError)
        if email:
            emailError = ''
            if '@' not in email:
                emailError = "Email must contain '@'"
    
            elif '.' not in email:
                emailError = "Email must contain one '.' "
    
            elif ' ' in email:
                emailError = "Email cannot contain space"
    
            
            periodCount = 0
            for char in email:
                if char == '.':
                    periodCount += 1
            if periodCount > 1:
                emailError = "Email must contaion only one '.'"
            if emailError != '':
                errors.append('uiEmail=' + emailError)
        if errors:
            print('errors =', errors)
            redirectString= redirectString + '&'.join(errors)
            print('joinedRedirectString=', redirectString)
            print('redirectString =', redirectString)
            return redirect(redirectString)
        else:
            return render_template('success.html', username=username)
    else:
        UsernameValue = request.args.get("usernameError", '')
        uiUsername = UsernameValue
        print('UsernameValue=', UsernameValue)
        PasswordValue = request.args.get("passwordError", '')
        uiPassword = PasswordValue
        print('PasswordValue=', PasswordValue)
        VerifyValue = request.args.get("verifyError", '')
        print('VerifyValue=', VerifyValue)
        uiEmail = request.args.get("uiEmail",'')
        print('uiEmail=', uiEmail)
        return render_template('signup.html', UsernameValue=UsernameValue, PasswordValue=PasswordValue, VerifyValue=VerifyValue, uiPassword=uiPassword, uiEmail=uiEmail)


if __name__ == "__main__":
    app.run()