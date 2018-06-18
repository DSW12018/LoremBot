import json
from ..object import Object

class Base(Object):

    @property
    def as_json(self):
        return json.dumps(self.__dict__)
