from pydantic import BaseModel


class TextMessage(BaseModel):
    type: str = "text"
    text: str


class ImageMessage(BaseModel):
    type: str = "image"
    url: str
    text: str | None = None


class ChatPayload(BaseModel):
    message: TextMessage | ImageMessage


def test_chat_message_parsing():
    api_response = {
        "message": {
            "type": "image",
            "text": "Custom text message"
        }
    }
    chat = ChatPayload.model_validate(api_response)
    assert chat.message.type == "image"
