from dataclasses import dataclass


@dataclass
class Chat:
    id: int
    created: str
    participant: list
    status: int
    message: list

    def to_dict(self):
        ...

    def from_dict(self):
        ...

