class ObserverBase(object):

    update = None

    def __init__(self):
        pass

    def update(self, update):
        self.update = update

    def call_strategy(update):
        pass


# Messaging Observer
# Client of strategy
class Messaging(ObserverBase):

    def __init__(self, strategy=None):
        pass

class InlineQuery(ObserverBase):
    pass

class CallbackQuery(ObserverBase):
    pass

class Payments(ObserverBase):
    pass
