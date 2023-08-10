from dataclasses import dataclass


@dataclass
class MessageContent:
    id: int
    message_type: int
    message_text: str
    message_code: str
    message_voice: int
    message_video: dict
    message_picture: dict
    message_file: dict

    def to_dict(self):
        ...

    def from_dict(self):
        ...


@dataclass
class Message:
    id: int
    id_chat: int
    sort_num: int
    send_user: int
    received_user: int
    send_datetime: str
    received_datetime: str
    message_content: int

    def to_dict(self):
        ...

    def from_dict(self):
        ...
