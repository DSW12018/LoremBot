from .base import Base


class KeyboardButton(Base):

    REQUIRED = [
        'text'
    ]

    OPTIONAL = [
        'request_contact',
        'request_location'
    ]
