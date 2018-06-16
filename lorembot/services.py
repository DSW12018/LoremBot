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
    def notify(self, update):
        for observer in self._observers
            observer.update(update)

class SubjectTelegram(SubjectService):

    _ENDPOINT = "https://api.telegram.org/"
    _STOP_FETCHING = False

    def __init__(self):
        # Read config file to get token
        self._TOKEN = ""  # get token from file
        self.BOT_ENDPOINT = "{}/{}".format(self._ENDPOINT, self._TOKEN)

    """
    Fetches updates from telegram api.
    """
    def fetch_updates():
        updates_url = "{}/getUpdates?timeout=100".format(self.BOT_ENDPOINT)
        while True:
            if self._STOP_FETCHING:
                return

            updates = []  # Actually make the request
            for update in updates:
                self.notify(update)

    """
    Stops a subject from fecthing updates from telegram api.
    """
    def stop_fetching():
        self._STOP_FETCHING = True
