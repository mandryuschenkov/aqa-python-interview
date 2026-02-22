import time
import pytest
from loguru import logger

def fetch_users_from_api():
    """Эмулирует долгий HTTP-запрос"""
    logger.debug("[API CALL] Fetching users...")
    time.sleep(2)
    return ["Alice", "Bob", "Charlie"]


class TestUserProfiles:

    @pytest.mark.parametrize("user", fetch_users_from_api())
    def test_profile_access(self, user):
        assert isinstance(user, str)
