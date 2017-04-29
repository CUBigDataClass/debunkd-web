class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'elb.bda.esu.io'

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'elb.bda.esu.io'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'elb.bda.esu.io'
