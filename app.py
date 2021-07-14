from configs.configs import JWTConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from queues.broker.broker import *
from configs.configs import *
import json
from configs.flask_config.flask_config import *
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

db = SQLAlchemy(app)
#import any models here
from sqlalchemy_models.models import *
db.create_all()

broker: Broker
if app.config.get("QUEUE_BROKER_URI") is not None:
    broker = Broker(app)
#import any queues here
    broker.create_all()



#add an import to any route folders here
from routes.login_register_routes import *
