import json
from .telegram.types import Document
from .command_handler import CommandHandler
class ObserverBase(object):

    def __init__(self):
        pass

# Messaging Observer
# Client of strategy
class Messaging(ObserverBase):

    def receive(self, update):
        if 'message' in update:
            self.call_strategy(update['message'])
    
    def call_strategy(self, message):
        if 'audio' in message:
            pass
            # Audio.from_json(message)
        elif 'text' in message and message['text'][0:1] == '/':
            CommandHandler.match(message['text'], message)
        elif 'text' in message:
            #Text.from_json(message)
            pass
        elif 'document' in message:
            pass
            #Document.from_json(message['document'])

# Adds capability to receive queries
class InlineQuery(ObserverBase):
    pass

# Adds capability to receive responses
class CallbackQuery(ObserverBase):
    pass

# Adds capability to receive payments
class Payments(ObserverBase):
    pass
