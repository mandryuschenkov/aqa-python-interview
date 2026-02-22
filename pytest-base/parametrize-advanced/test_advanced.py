import pytest
from loguru import logger


@pytest.fixture(scope="module")
def db_connection(request):
    logger.debug(f"Open connection for user: {request.param}")
    yield f"Connection_Object_{request.param}"
    logger.debug(f"Close connection for user: {request.param}")


class TestDatabaseAccess:

    @pytest.mark.parametrize("db_connection", ["admin", "guest"], indirect=True)
    def test_read_data(self, db_connection):
        logger.debug(f"Reading data using {db_connection}")
        assert "Connection_Object" in db_connection

    @pytest.mark.parametrize("db_connection", ["admin", "guest"], indirect=True)
    def test_write_data(self, db_connection):
        logger.debug(f"Writing data using {db_connection}")
        assert "Connection_Object" in db_connection

    @pytest.mark.parametrize("db_connection", ["admin"], indirect=True)
    def test_delete_data(self, db_connection):
        logger.debug(f"Deleting data using {db_connection}")
        assert "Connection_Object" in db_connection
