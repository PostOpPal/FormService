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

from  mongoengine import connect
connect(host=app.config.get("MONGODB_URL"))

#broker: Broker
#if app.config.get("QUEUE_BROKER_URI") is not None:
#    broker = Broker(app)

#add an import to any route folders here
from routes.user_form_routes import *
from routes.doctor_routes import *

@app.route('/', methods = ['GET'])
def get_root():
    return "Form Service API"