""" test api endpoints """

from fastapi.testclient import TestClient
from {{cookiecutter.project_slug}}.api import app

client = TestClient(app)

def test_root_get():
    """ test root GET endpoint """
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"title": "new project",
            "method": "GET"}

def test_root_post():
    """ test root POST endpoint """
    response = client.post('/')
    assert response.status_code == 200
    assert response.json() == {"title": "new project",
            "method": "POST"}
