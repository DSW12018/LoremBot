from .base import Base

class Document(Base):

    REQUIRED = [
        'file_id'
    ]

    OPTIONAL = [
        'thumb',
        'file_name',
        'mime_type',
        'file_size'
    ]
