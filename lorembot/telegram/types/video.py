from .base import Base

class Video(Base):

    REQUIRED = [
        'file_id',
        'width',
        'height',
        'duration'
    ]

    OPTIONAL = [
        'thumb',
        'mime_type',
        'file_size'
    ]
