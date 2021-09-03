from fastapi import FastAPI

app = FastAPI()

# TODO connect broker and connect to mongoengine

# if os.environ.get("DEPLOY") == "test":
#     print()
#     print("Testing")
#     app.config.from_object(TestConfig)

# elif os.environ.get("DEPLOY") == "local":
#     print()
#     print("Local")
#     app.config.from_object(LocalConfig)

# else:
#     print("Deployment")
#     app.config.from_object(DeploymentConfig)

#broker: Broker
#if app.config.get("QUEUE_BROKER_URI") is not None:
#    broker = Broker(app)

#add an import to any route folders here
from routes.user_form_routes import *
from routes.doctor_routes import *

@app.get('/')
def get_root():
    return {"message":"Form Service API"}