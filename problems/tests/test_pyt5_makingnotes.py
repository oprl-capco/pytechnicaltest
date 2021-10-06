# Your answers in pyt5_makingnotes.py must pass these tests
# Do not modify the unit tests

from fastapi.testclient import TestClient

from problems.pyt5_makingnotes import app

client = TestClient(app)


class TestClass5:

    def test_should_make_note(self):
        response = client.get("/exercise/?note=the quick fox&mag=the quick brown fox")
        assert response.status_code == 200
        assert response.json() == {"canMakeNote": "True"}

    def test_should_not_make_note(self):
        response = client.get("/exercise/?note=the quick brown fox&mag=the quick fox")
        assert response.status_code == 200
        assert response.json() == {"canMakeNote": "False"}
