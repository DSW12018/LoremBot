class SubjectService(object):

    def __init__(self):
        self._observers = []

    """
    Attach an observer to subject service.
    """
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    """
    Detach an observer from subject service.
    """
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    """
    Notify all observers.
    """
    def notify(self):
        for observer in self._observers
            observer.update(self)
