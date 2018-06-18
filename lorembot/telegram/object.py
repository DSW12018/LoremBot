class Object(object):
    REQUIRED = []
    OPTIONAL = []

    def __init__(self, *args, **kwargs):
        # required
        self.build_required(kwargs)
        # optional
        self.build_optional(kwargs)

    def build_required(self, *args, **kwargs):
        for required in REQUIRED:
            self[required] = kwargs[required]

    def build_optional(self, *args, **kwargs):
        for optional in OPTIONAL:
            if optional in kwargs:
                self[optional] = kwargs[optional]
            else:
                self[optional] = None
