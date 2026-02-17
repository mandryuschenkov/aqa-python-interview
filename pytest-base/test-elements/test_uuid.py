import requests


class TestUUID:

    def test_get_uuid(self):
        resp = requests.get("https://httpbin.org/uuid")
        assert resp.status_code == 200
        assert "uuid" in resp.json()
