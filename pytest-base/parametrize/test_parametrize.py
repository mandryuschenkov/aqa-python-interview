import pytest


class TestUserAge:

    @pytest.mark.parametrize("age, expected", [
        (17, False),
        (18, True),
        (19, True),
    ])
    def test_is_adult(self, age, expected):
        def is_adult(value):
            return value >= 18

        assert is_adult(age) == expected

    @pytest.mark.parametrize("user", [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 15},
    ])
    def test_user_processing(self, user):
        assert isinstance(user["name"], str)
        assert isinstance(user["age"], int)
