from .config import config

class Settings(object):

    def __init__(self, *args, **kwargs):
        config.load_settings(kwargs)