# Your answers in pyt4_caseconverter.py must pass these tests
# Do not modify the unit tests

from fastapi.testclient import TestClient

from problems.pyt4_caseconverter import app

client = TestClient(app)


class TestClass4:

    def test_should_be_camel(self):
        response = client.get("/exercise/camel/this_method")
        assert response.status_code == 200
        assert response.json() == {"CamelCase": "ThisMethod"}

    def test_should_be_snake(self):
        response = client.get("/exercise/snake/ThisMethod")
        assert response.status_code == 200
        assert response.json() == {"snake_case": "this_method"}
