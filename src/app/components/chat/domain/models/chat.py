from src.components.chat.domain.models.chat_id import ChatId


class RootEntity:
    pass


class ParticipantChat:
    pass


class HistoryChat:
    pass


class StatusChat:
    pass


class Chat(RootEntity):
    id = ChatId
    participants = ParticipantChat
    history = HistoryChat
    created = str
    statut = StatusChat
