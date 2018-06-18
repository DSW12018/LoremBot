import json
from .base import Base

class Contact(Base):

    def __init__(self, *args, **kwargs):
        # required
        self.phone_number = kwargs['phone_number']
        self.first_name = kwargs['first_name']
        # optional
        self.last_name = kwargs['last_name']
        self.user_id = kwargs['user_id']
