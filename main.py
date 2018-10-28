from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


app.run()
