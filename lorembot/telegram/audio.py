import json
from .type_base import TypeBase

class Audio(TypeBase):

    def __init__(self, *args, **kwargs):
        # required
        self.file_id = kwargs['file_id']
        self.duration = kwargs['duration']
        # optional
        self.performer = kwargs['performer']
        self.title = kwargs['title']
        self.mime_type = kwargs['mime_type']
        self.file_size = kwargs['file_size']
