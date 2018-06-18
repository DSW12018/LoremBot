from .base import Base

class Contact(Base):

    REQUIRED = [
        'phone_number',
        'first_name'
    ]

    OPTIONAL = [
        'last_name',
        'user_id'
    ]
