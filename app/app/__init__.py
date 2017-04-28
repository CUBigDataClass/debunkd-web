from flask import Flask
from cassandra.cluster import Cluster

example = 'TESTING R2D2T2B2'
# sbweb_db = Cluster(['127.0.0.1'], port=9042)
app = Flask(__name__)

from . import views
