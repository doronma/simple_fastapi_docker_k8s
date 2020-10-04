from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_ping():
    response = client.get("/ping", headers={"token": "atoken"})
    assert response.status_code == 200
    assert response.json() == {"message": "ping ok", "token": "atoken"}


def test_ping_error():
    response = client.get("/ping")
    assert response.status_code == 422


def test_post_person():
    json = {
        "id": "3",
        "name": "aviv",
        "joined": "2018-07-21"
    }
    response = client.post("http://127.0.0.1:8000/persons/4", json=json)
    assert response.status_code == 201
    assert response.json() == {"msg": "ok"}
