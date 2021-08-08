from flask import Flask
from configs.configs import *
from configs.flask_config.flask_config import *
from configs.configs import mongoConfig
import os

app = Flask(__name__, instance_relative_config=True)

if os.environ.get("DEPLOY") == "test":
    print()
    print("Testing")
    app.config.from_object(TestConfig)

elif os.environ.get("DEPLOY") == "local":
    print()
    print("Local")
    app.config.from_object(LocalConfig)

else:
    print("Deployment")
    app.config.from_object(DeploymentConfig)

# mongo db
import pymongo 
mongo_client = pymongo.MongoClient(app.config.get("MONGODB_URL"))
db = mongo_client[mongoConfig.database]
users_collection = db[mongoConfig.user_collection]


#broker: Broker
#if app.config.get("QUEUE_BROKER_URI") is not None:
#    broker = Broker(app)
    #import any queues here
#    broker.create_all()

#add an import to any route folders here
from routes.user_form_routes import *

@app.route('/', methods = ['GET'])
def get_root():
    return "Form Service API"