from flask import Flask, request, render_template, url_for
from . import app

@app.route('/', methods=['get'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/about', methods=['get'])
def about():
    if request.method == 'GET':
        return render_template('about.html')
