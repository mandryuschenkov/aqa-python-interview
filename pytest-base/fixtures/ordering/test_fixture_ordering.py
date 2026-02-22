import pytest
from loguru import logger


@pytest.fixture(scope="session")
def setup_1():
    logger.debug(1)
    yield
    logger.debug(2)


@pytest.fixture(autouse=True)
def setup_2(setup_1):
    logger.debug(3)
    yield
    logger.debug(4)


@pytest.fixture
def setup_3():
    logger.debug(5)
    yield
    logger.debug(6)


@pytest.fixture
def setup_4(setup_3):
    logger.debug(7)


class TestFixtureOrdering:

    def test_one(self, setup_4):
        logger.debug(8)
        assert True

    def test_two(self):
        logger.debug(9)
        assert False
