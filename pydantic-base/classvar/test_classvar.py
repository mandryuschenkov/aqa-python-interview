from typing import ClassVar
from pydantic import BaseModel


class ConfigModel(BaseModel):
    FIELD_LABELS: ClassVar[dict[str, str]] = {
        "prefix": "model:",
        "version": "1.0",
    }

    first_name: str
    last_name: str
    email: str


def test_classvar_not_a_field():
    model = ConfigModel(first_name="Ivan", last_name="Petrov", email="ivan@test.com")
    assert model.FIELD_LABELS == {
        "prefix": "model:",
        "version": "1.0",
    }
    assert model.model_dump() == {
        "first_name": "Ivan",
        "last_name": "Petrov",
        "email": "ivan@test.com",
    }
    assert "FIELD_LABELS" not in ConfigModel.model_fields
