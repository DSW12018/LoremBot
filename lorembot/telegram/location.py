from .type_base import TypeBase

class Location(TypeBase):

    def __init__(self, *args, **kwargs):
        self.longitude = kwargs['longitude']
        self.latitude = kwargs['latitude']
