# Do not modify the unit tests

from fastapi.testclient import TestClient

from problems.pyt5_makingnotes import app

client = TestClient(app)


def test_should_say_hello():
    response = client.get("/exercise/?note=the quick fox&mag=the quick brown fox")
    assert response.status_code == 200
    assert response.json() == {"canMakeNote": "True"}

    response = client.get("/exercise/?note=the quick brown fox&mag=the quick fox")
    assert response.status_code == 200
    assert response.json() == {"canMakeNote": "False"}