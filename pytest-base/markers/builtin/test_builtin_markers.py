import pytest

API_CONFIG = {"version": 1}


@pytest.fixture(autouse=True)
def setup_api_version():
    API_CONFIG["version"] = 2


@pytest.mark.skipif(API_CONFIG["version"] < 2, reason="Требуется API v2")
def test_api_v2_feature():
    assert True


@pytest.mark.xfail(reason="Баг JIRA-123", strict=True)
def test_flaky_endpoint():
    # Имитация починенного бага
    response_status = 200
    assert response_status == 200


@pytest.mark.skip(reason="Устаревший функционал")
def test_deprecated_feature():
    assert False


def test_dynamic_skip():
    if API_CONFIG["version"] == 2:
        pytest.skip("Пропуск в рантайме")
    assert True
