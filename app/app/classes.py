

class Query():
    """
    Object to contain query and query results
    """

    def __init__ (self, query="", query_return=None, topic=None):
        self.query = query
        self.topic = topic
        self.query_results = query_return
        self.cquery = None
        self.states = dict.fromkeys([ 'ma', 'wa', 'ca', 'or', 'wi', 'me', 'mi', 'nv', 'nm', 'co', 'wy', 'co', 'wy', 'ks', 'ne', 'ok', 'mo', 'il', 'in', 'vt', 'ar', 'tx', 'ri', 'al', 'ms', 'nc', 'va', 'ia', 'md', 'de', 'pa', 'nj', 'ny', 'id', 'sd', 'ct', 'nh', 'ky', 'oh', 'tn', 'wv', 'dc', 'la', 'fl', 'ga', 'sc', 'mn', 'mt', 'nd', 'az', 'ut', 'hi', 'ak' ])
        self.map_data = None
        self.timechart_data = None
        self.tweet_data = None

    def set_cquery(self, topic_num):
        """
        Given the topic number corresponding to relevant topic,
        create and store the query into this class
        """
        self.cquery = "SELECT * FROM SOME_TABLE WHERE " + str(topic_num)
