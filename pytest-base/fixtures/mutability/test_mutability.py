import pytest


@pytest.fixture(scope="module")
def user_session_data():
    return {
        "username": "admin",
        "role": "manager",
        "token": "valid_token_123"
    }


def test_admin_can_refresh_token(user_session_data):
    new_token = "refreshed_token_456"
    user_session_data.update({"token": new_token})
    assert user_session_data["token"] == new_token


def test_admin_has_valid_initial_token(user_session_data):
    assert user_session_data["token"] == "valid_token_123"
