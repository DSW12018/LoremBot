class BehaviorBase(object):

    update = None

    def __init__(self):
        pass

    def update(self, update):
        self.update = update

class Messaging(BehaviorBase):
    pass
