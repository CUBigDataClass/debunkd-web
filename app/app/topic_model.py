from collections import Counter
import operator

class Topic_model:

    def __init__(self):
        self.topics = [ \
            Counter('being single disability'.split(' ')), \
            Counter('chemotherapy doctor blows whistle doesnt work'.split(' ')), \
            Counter('emails released by wikileaks confirm hillary clinton sold weapons to isis'.split(' ')), \
            Counter('el chapo put a 100 millon bounty donald trump'.split(' ')), \
            Counter('eddie murphy death hox died'.split(' ')), \
            Counter('hillary clinton assistant j.w. j.w mcgill dead'.split(' ')), \
            Counter('michelle obama file filed divorce mistress'.split(' ')), \
            Counter('buzz aldrin apollo fake apollo space mission moon landing'.split(' ')), \
            Counter('barack obama birth certificate forgery forged fake'.split(' '))]
        self.links = ['http://www.snopes.com/being-single-is-a-disability/', \
            'http://www.snopes.com/chemotherapy-doctor-blows-the-whistle/', \
            'http://www.snopes.com/wikileaks-cofirms-hillary-clinton-sold-weapons-to-isis/', \
            'http://www.snopes.com/el-chapo-donald-trump-bounty/', \
            'http://www.snopes.com/eddie-murphy-death-hoax/', \
            'http://www.snopes.com/clinton-mcgill-found-dead/', \
            'http://www.snopes.com/obamas-divorce-pregnant-mistress/', \
            'http://www.snopes.com/media/notnews/buzzaldrin.asp', \
            'http://www.snopes.com/politics/obama/birthers/birthcertificate.asp']

    def best_topic(self, query):
        """
        Given a query, return the number corresponding to the most closely
        associated topic
        : param query: string containing user query
        """

        query = query.lower()
        topic_score = {}
        for topic in enumerate(self.topics):
            score = 0
            for qword in query.split(' '):
                if qword in topic[1]: score += self.topics[topic[0]][qword]
            topic_score[topic[0]] = score

        top_index = max(topic_score.items(), key=operator.itemgetter(1))[0]
        return top_index, self.links[top_index]


topics_lib = Topic_model()
