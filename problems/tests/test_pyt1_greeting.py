# Your answers in pyt1_greeting.py must pass these tests
# Do not modify the unit tests

from fastapi.testclient import TestClient

from problems.pyt1_greeting import app

client = TestClient(app)


class TestClass1:
    def test_should_say_hello(self):
        response = client.get("/exercise/Capco")
        assert response.status_code == 200
        assert response.json() == {"greeting": "Hello, Capco!"}
