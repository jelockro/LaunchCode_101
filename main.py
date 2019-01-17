from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/signup", methods=['POST'] )
def signup():
    print(request.form)
    input_fields = { 'Username': '', 'Password': '',
    'Email (optional)': ''}
    errors = []
    blank_error = "{0} can't be left blank"
    for key in request.form:
        if key in input_fields:
            input_fields[key] = request.form[key]
    print(input_fields)

    #print(username)
    #print(request.form)
    username = input_fields['Username']
    if username:
        username_escaped = cgi.escape(username)
        return render_template('success.html', username=username_escaped)
    else:
        errors.append('username_error')
        return redirect("/?error=" + blank_error.format('Username') )


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error)
app.run()
