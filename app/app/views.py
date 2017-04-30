from flask import Flask, request, render_template, url_for, redirect
from app import app
from app.classes import Query
from app.topic_model import topics_lib

prefork_driver = True

try:
    from app import cassandra_driver
except ImportError:
    from app import sbdb
    prefork_driver = False

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
            # Get the topic number and relevant snopes link
            uquery.topic = topics_lib.best_topic(uquery.query)

            # uquery.set_cquery(topic_num)
            # Get generators from cassandra for visualizations
            get_data(uquery)
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

    # Construct cassandra queries
    map_query = "SELECT location, count FROM state_aggregates WHERE topic = '{}'".format(uquery.topic[0])
    tc_query = "SELECT posted_time, count FROM date_aggregates WHERE topic = '{}'".format(uquery.topic[0])

    tweet_query = "SELECT posted_time, body FROM tweets_master WHERE topic = '{}' LIMIT 500 ALLOW FILTERING".format(uquery.topic[0])

    if prefork_driver:
        conn = cassandra_driver.conn
    else:
        conn = sbdb

    uquery.map_data = conn.execute(map_query)
    uquery.timechart_data = conn.execute(tc_query)
    uquery.tweet_data = conn.execute(tweet_query)
