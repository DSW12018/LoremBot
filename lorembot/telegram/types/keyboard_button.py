from .base import Base


class KeyboardButton(Base):

    def __init__(self, **kwargs):
        self.text = kwargs['text']
        self.request_contact = kwargs['request_contact']
        self.request_location = kwargs['request_location']
