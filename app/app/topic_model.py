from collections import Counter
import operator

class Topic_model:

    def __init__(self):
        self.topics = [ \
            Counter('being single disability'.split(' ')), \
            Counter('emails released by wikileaks confirm hillary clinton sold weapons to isis'.split(' ')), \
            Counter('chemotherapy doctor blows whistle doesnt work'.split(' ')), \
            Counter('el chapo put a 100 millon bounty donald trump'.split(' '))]
        self.links = ['http://www.snopes.com/being-single-is-a-disability/', \
            'http://www.snopes.com/wikileaks-cofirms-hillary-clinton-sold-weapons-to-isis/', \
            'http://www.snopes.com/chemotherapy-doctor-blows-the-whistle/', \
            'http://www.snopes.com/el-chapo-donald-trump-bounty/']

    def best_topic(self, query):
        query = query.lower()
        topic_score = {}
        for topic in enumerate(self.topics):
            score = 0
            for qword in query.split(' '):
                if qword in topic[1]: score += 1
            topic_score[topic[0]] = score

        top_index = max(topic_score.items(), key=operator.itemgetter(1))[0]
        return top_index, self.links[top_index]


topics_lib = Topic_model()
