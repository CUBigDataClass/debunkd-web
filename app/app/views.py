from flask import Flask, request, render_template, url_for, redirect
from . import app

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    if request.method == 'GET':
        return render_template('about.html')

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        query = request.form['search']
        url = '/search/' + query
        print(url)
        if query:
            # return redirect(url)
            return render_template('adindex.html', query=query)
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route('/map', methods=['GET', 'POST'])
def map():
    if request.method == 'POST':
        pass
    else:
        return render_template('mapsearch.html')
