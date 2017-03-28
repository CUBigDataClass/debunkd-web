from flask import Flask, request, render_template, url_for, redirect
from . import app

@app.route('/', methods=['get'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/about', methods=['get'])
def about():
    if request.method == 'GET':
        return render_template('about.html')

@app.route('/search', methods=['post'])
def search():
    query = request.form['search']
    print("Text in search box: '", query, "'")
    return redirect('/')
