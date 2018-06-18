class TObject(dict):
    REQUIRED = []
    OPTIONAL = []
    IGNORE = []

    def __getattr__(self, item):
        return self[item]

    def __init__(self, **kwargs):
        # required
        self.build_required(**kwargs)
        # optional
        self.build_optional(**kwargs)

    def build_required(self, **kwargs):
        for required in self.REQUIRED:
            self[required] = kwargs[required]

    def build_optional(self, **kwargs):
        for optional in self.OPTIONAL:
            if optional in kwargs and not optional in self.IGNORE:
                self[optional] = kwargs[optional]
            else:
                self[optional] = None
