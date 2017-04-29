from flask import Flask
from cassandra.cluster import Cluster
from . import configmodule

app = Flask(__name__)
app.config.from_object('app.configmodule.DevelopmentConfig')
from . import views
