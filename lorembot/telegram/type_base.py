import json

class TypeBase(object):

    @property
    def as_json(self):
        return json.dumps(self.__dict__)
