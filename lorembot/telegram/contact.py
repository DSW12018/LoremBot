import json
from .type_base import TypeBase

class Contact(TypeBase):

    def __init__(self, *args, **kwargs):
        # required
        self.phone_number = kwargs['phone_number']
        self.first_name = kwargs['first_name']
        # optional
        self.last_name = kwargs['last_name']
        self.user_id = kwargs['user_id']
