class TestConfig(object):
    SECRET_KEY = 'test'
    MONGODB_URL = "mongodb://localhost:27017/FormService"
    #QUEUE_BROKER_URI= 'localhost'

class LocalConfig(object):
    SECRET_KEY = 'test'
    MONGODB_URL = "mongodb://localhost:27017/FormService"
    #QUEUE_BROKER_URI = 'localhost'

class DeploymentConfig(object):
    #TODO should be taken from environment variable
    SECRET_KEY = 'test'
    #TODO should be set to point at the location of the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGODB_URL = ""
    #QUEUE_BROKER_URI = 'localhost'
