class Message(object):

    def __init__(self, message):
        self.build(message)

    def build(self, message):
        raise Exception

class Command(Message):
    def build(self, message):
        pass

class TextMessage(Message):

    def build(self, message):
        self.text = message['text']

class Location(Message):
    def build(self, message):
        pass

class Contact(Message):
    def build(self, message):
        pass

class Voice(Message):
    def build(self, message):
        pass

class Document(Message):
    def build(self, message):
        pass
