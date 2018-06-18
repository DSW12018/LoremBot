api = "https://api.telegram.org/bot"

class Config(object):

    def __init__(self):
        pass

    def load_settings(self, settings):
        self.commands = settings['commands']
        self.timeout = settings['timeout']
        self.interval = settings['interval']
        self.uri = api + settings['token']


config = Config()