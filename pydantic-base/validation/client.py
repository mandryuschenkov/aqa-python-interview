from uuid import uuid4
from typing import Literal
from pydantic import BaseModel, Field, EmailStr, UUID4


class Contact(BaseModel):
    phone: str
    email: EmailStr
    telegram: str | None = None


class Client(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    middle_name: str
    is_active: bool = True
    contact: Contact
    age: int = Field(..., ge=18, le=80)
    status: Literal[1, 2, 3]


client_dict = {
    "first_name": "Ivan",
    "last_name": "Petrov",
    "is_active": 1,
    "age": "18",
    "gender": "male",
    "status": "1",
    "contact": {
        "phone": "+79998887766",
        "email": "email@testcom"
    }
}

client = Client.model_validate(client_dict)
