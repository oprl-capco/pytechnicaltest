# Your answers in pyt2_nameserver.py must pass these tests
# Do not modify the unit tests

from fastapi.testclient import TestClient

from problems.pyt2_nameserver import app

client = TestClient(app)


class TestClass2:
    def test_should_post(self):
        response = client.post("/exercise/?firstname=John&lastname=Doe")
        assert response.status_code == 200
        assert response.json() == "Added: " + str({1: {"firstname": "John", "lastname": "Doe"}})

    def test_should_get(self):
        client.post("/exercise/?firstname=Jane&lastname=Doe")
        client.post("/exercise/?firstname=Foo&lastname=Bar")

        response = client.get("/exercise/3")
        assert response.status_code == 200
        assert response.json() == "Retrieved: " + str({3: {"firstname": "Foo", "lastname": "Bar"}})

    def test_should_not_get(self):
        response = client.get("/exercise/123")
        assert response.status_code == 404
