from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/signup", methods=['POST'] )
def signup():
    errors = []
    error = "{0} can't be left blank"
    username = request.form['Username']
    #print(username)
    #print(request.form)
    if username:
        username_escaped = cgi.escape(username)
    else:
        errors.append('username_error')
        return redirect("/?error=" + error.format('Username') )

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error)
app.run()
