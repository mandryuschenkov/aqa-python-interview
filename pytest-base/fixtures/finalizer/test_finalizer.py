import pytest
from loguru import logger


@pytest.fixture
def resource_a(request):
    logger.debug(1)
    request.addfinalizer(lambda: logger.debug(2))
    logger.debug(3)
    request.addfinalizer(lambda: logger.debug(4))


@pytest.fixture(autouse=True)
def resource_b():
    logger.debug(5)
    yield
    logger.debug(6)


@pytest.fixture
def resource_c(resource_a, request):
    logger.debug(7)
    request.addfinalizer(lambda: logger.debug(8))
    raise Exception("Critical Error in Setup C")
    logger.debug(9)
    yield
    logger.debug(10)


class TestFinalizers:

    def test_one(self, resource_c):
        logger.debug(11)
        assert True
