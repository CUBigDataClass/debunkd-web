

class Query():
    """
    Object to contain query and query results
    """

    def __init__ (self, query="", query_return=None):
        self.query = query
        self.query_results = query_return
        self.states = dict.fromkeys([ 'ma', 'wa', 'ca', 'or', 'wi', 'me', 'mi', 'nv', 'nm', 'co', 'wy', 'co', 'wy', 'ks', 'ne', 'ok', 'mo', 'il', 'in', 'vt', 'ar', 'tx', 'ri', 'al', 'ms', 'nc', 'va', 'ia', 'md', 'de', 'pa', 'nj', 'ny', 'id', 'sd', 'ct', 'nh', 'ky', 'oh', 'tn', 'wv', 'dc', 'la', 'fl', 'ga', 'sc', 'mn', 'mt', 'nd', 'az', 'ut', 'hi', 'ak' ])
