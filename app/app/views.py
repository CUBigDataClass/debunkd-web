from flask import Flask, request, render_template, url_for, redirect
from app import app
from app.classes import Query

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
        uquery = Query()
        uquery.query = request.form['search']
        uquery.query_results = "Query results of: "
        if uquery.query:
            # return redirect(url)
            return render_template('adindex.html', uquery=uquery)
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
