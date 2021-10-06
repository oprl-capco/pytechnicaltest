# Your answers in pyt4_linspacearray.py must pass these tests
# Do not modify the unit tests

from fastapi.testclient import TestClient

from problems.pyt3_arraysubsets import app

client = TestClient(app)


class TestClass4:
    def test_should_be_linspace(self):
        response = client.get("/exercise/1/4/4")
        assert response.status_code == 200
        assert response.json() == {"array": "[1, 2, 3, 4]"}

    def test_should_be_linspace_and_float(self):
        response = client.get("/exercise/1/2/5")
        assert response.status_code == 200
        assert response.json() == {"array": "[1, 1.25, 1.5, 1.75, 2]"}

