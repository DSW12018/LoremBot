from .base import Base


class Location(Base):

    def __init__(self, *args, **kwargs):
        self.longitude = kwargs['longitude']
        self.latitude = kwargs['latitude']
