from flask import Flask
from cassandra.cluster import Cluster

example = 'TESTING R2D2T2B2'
# sbweb_db = cluster.connect('swashbucklers')
app = Flask(__name__)

from . import views
