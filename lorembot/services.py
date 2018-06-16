from utils import JSONRequest
import time
from behaviour import BehaviorBase

class SubjectService(object):

    _observers = []

    def __init__(self):
        pass

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
        for observer in self._observers:
            BehaviorBase.update(observer, update)

class SubjectTelegram(SubjectService):

    _ENDPOINT = "https://api.telegram.org/bot"
    _STOP_FETCHING = False
    _TOKEN = "597378495:AAGXqZOta46LZ_7NhtqCpGp7i9JWaJ6gyV8"
    _TIMEOUT = 100

    def __init__(self):
        super(SubjectService, self).__init__()
        # Read config file to get token
        self.BOT_ENDPOINT = "{}{}".format(self._ENDPOINT, self._TOKEN)

    """
    Fetches updates from telegram api.
    """
    def fetch_updates(self):
        updates_url = "{}/getUpdates?timeout={}".format(
            self.BOT_ENDPOINT,
            self._TIMEOUT
        )

        while True:
            if self._STOP_FETCHING:
                return

            updates = JSONRequest.fetch(updates_url)

            if not 'result' in updates:
                pass

            for update in updates['result']:
                self.notify(update)
            time.sleep(0.5)

    """
    Stops a subject from fecthing updates from telegram api.
    """
    def stop_fetching(self):
        self._STOP_FETCHING = True
