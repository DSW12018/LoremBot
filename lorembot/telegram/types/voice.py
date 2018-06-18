from .base import Base

class Voice(Base):

    REQUIRED = [
        'file_id',
        'duration'
    ]

    OPTIONAL = [
        'mime_type',
        'file_size'
    ]
