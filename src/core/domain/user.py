from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    nicname: str
    phone: str
    avatar: int
    about: str

    def to_dict(self):
        ...

    def from_dict(self):
        ...
