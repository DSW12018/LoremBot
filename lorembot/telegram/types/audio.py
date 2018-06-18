import json
from .base import Base

class Audio(Base):
    
    REQUIRED = [
        'file_id',
        'duration',
    ]

    OPTIONAL = [
        'performer',
        'title',
        'mime_type',
        'file_size'
    ]