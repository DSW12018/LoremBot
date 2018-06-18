import time
from .config import config
from .utils import JSONRequest
from .observers import ObserverBase


class Service(object):

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
            ObserverBase.update(observer, update)

class TelegramService(Service):

    _STOP_FETCHING = False

    """
    Fetches updates from telegram api.
    """
    def fetch_updates(self):
        updates_url = "{}/getUpdates?timeout={}".format(
            config.uri,
            config.timeout
        )

        while True:
            if self._STOP_FETCHING:
                return

            updates = JSONRequest.fetch(updates_url)

            if not 'result' in updates:
                pass

            for update in updates['result']:
                self.notify(update)
            time.sleep(config.interval)

    """
    Stops a subject from fecthing updates from telegram api.
    """
    def stop_fetching(self):
        self._STOP_FETCHING = True
