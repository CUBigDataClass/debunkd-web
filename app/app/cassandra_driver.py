from uwsgidecorators import *
from cassandra.cluster import Cluster
from . import configmodule

conn = None

@postfork
def init_session():
    global conn
    cluster = Cluster(["elb.bda.esu.io"], port=9042)
    conn = cluster.connect('swashbucklers')
