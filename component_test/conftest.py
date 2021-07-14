import os
import tempfile

import pytest
from app import app 
#from flaskr.db import init_db


@pytest.fixture
def client():
    with app.test_client() as client:
        #with app.app_context():
        #    init_db()
        yield client