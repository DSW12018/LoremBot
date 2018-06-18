from .base import Base

class VideoNote(Base):

    REQUIRED = [
        'file_id',
        'length',
        'duration'
    ]

    OPTIONAL = [
        'thumb',
        'file_size'
    ]
