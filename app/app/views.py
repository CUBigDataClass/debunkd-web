from flask import Flask, request, render_template, url_for, redirect
from app import app, example 
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
        if uquery.query:
            # Get generators from cassandra for visualizations
            # get_data(uquery)
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

def get_data(uquery):
    """
    Given a user query, get relevant data from cassandra DB
    : param uquery: class containing the user query and variables
        to store generators for cassandra data
    """
    
    session = sbweb_db.connect('swashbucklers')
    
    # Figure out what query to make
    map_query = "SELECT * FROM tweets_master"
    timechart_query = "SELECT * FROM tweets_master"

    uquery.map_data = sbweb_db.execute(map_query)
    uquery.timechart_data = sbweb_db.execute('select * from tweets_master limit 10;')

    



