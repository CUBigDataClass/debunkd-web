from flask import Flask
from cassandra.cluster import Cluster
from . import configmodule

app = Flask(__name__)
app.config.from_object('app.configmodule.DevelopmentConfig')

cluster = Cluster([app.config['DATABASE_URI']], port=9042)
sbdb = cluster.connect('swashbucklers')

from . import views
