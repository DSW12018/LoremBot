import json
from ..tobject import TObject

class Base(TObject):

    @property
    def as_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, *args, **kargs):
        cls(json.loads(args))
