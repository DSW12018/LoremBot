import json
from ..tobject import TObject

class Base(TObject):

    @property
    def as_json(self):
        return json.dumps(self.__dict__)
