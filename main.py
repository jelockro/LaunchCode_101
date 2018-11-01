from flask import Flask, request, redirect, render_template
import cgi
import os

app=Flask(__name__
app.config['DEBUG'] = True

tasks =[]

@app.route('/todos', methods=['POST', 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('todos.html', title="TODOs")