from .base import Base

class User(Base):

    REQUIRED = [
        'id',
        'is_bot',
        'first_name',
    ]

    OPTIONAL = [
        'last_name',
        'username',
        'language_code',
    ]
