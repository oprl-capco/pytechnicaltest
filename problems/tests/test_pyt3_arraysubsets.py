# Your answers in pyt3_arraysubsets.py must pass these tests
# Do not modify the unit tests

from fastapi.testclient import TestClient

from problems.pyt3_arraysubsets import app

client = TestClient(app)


class TestClass3:
    def test_should_be_subset(self):
        response = client.get("/exercise/3,4,1,5,2,3/3,5,2")
        assert response.status_code == 200
        assert response.json() == {"isSubset": "True"}

    def test_should_not_be_subset(self):
        response = client.get("/exercise/3,4,1,5,2,3/3,8,2")
        assert response.status_code == 200
        assert response.json() == {"isSubset": "False"}
