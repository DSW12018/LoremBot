from .base import Base


class Location(Base):

    REQUIRED = [
        'latitude',
        'longitude'
    ]
