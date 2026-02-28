import requests


class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.params = {"api_version": "v1"}
        self.session.headers.update({"X-Source": "MobileApp", "User-Agent": "QA-Bot/1.0"})
        self.session.auth = ("admin", "supersecret123")

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def test_session_merging_logic():
    with APIClient() as client:
        response = client.session.get(
            url="https://httpbin.org/anything?filter=active",
            params={"api_version": "v2", "limit": 100},
            headers={"User-Agent": None},
            auth=("guest", "guest_pass")
        )
    assert response.status_code == 200
