import os
import uuid
import pytest

TOKEN_FILE = "token.txt"

@pytest.fixture(scope="session")
def auth_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            token = f.read()
            if token:
                return token
            
    token = str(uuid.uuid4())
    with open(TOKEN_FILE, "w") as f:
        f.write(token)
        
    return token


def test_user_profile(auth_token):
    with open(TOKEN_FILE, "r") as f:
        assert auth_token == f.read()


def test_user_settings(auth_token):
    with open(TOKEN_FILE, "r") as f:
        assert auth_token == f.read()


def test_user_billing(auth_token):
    with open(TOKEN_FILE, "r") as f:
        assert auth_token == f.read()


def test_user_history(auth_token):
    with open(TOKEN_FILE, "r") as f:
        assert auth_token == f.read()
