import pytest

test_data = [
    ("admin", "12345", 200),
    ("guest", "pass", 403),
    pytest.param("banned", "qwerty", 403, marks=pytest.mark.skip(reason="Account locked in DB")),
    pytest.param("test_user", "test", 200, marks=pytest.mark.xfail(strict=True, reason="Bug JIRA-777"))
]


@pytest.mark.parametrize("login, password, expected_status", test_data)
def test_login_api(login, password, expected_status):
    # Имитация запроса к API
    actual_status = 200 if login in ("admin", "test_user") else 403
    assert actual_status == expected_status
