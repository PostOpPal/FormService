from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


app = FastAPI()
from  mongoengine import connect
connect(host="mongodb://localhost:27017/FormService")

#add an import to any route folders here
from routes.user_form_routes import *
from routes.doctor_routes import *
from routes.debug_routes import *

@app.get('/')
def get_root():
    return {"message":"Form Service API"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="PostOpPal FormService Docs",
        version="0.0.1",
        description="Documentation for the PostOpPal FormService routes",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

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