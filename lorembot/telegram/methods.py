import requests
import json
from lorembot.config import uri

class BaseMethod(object):

    RESTRICTED = []

    def __init__(self, *args, **kwargs):
        # required
        self.build_required(kwargs)
        # optional
        self.build_optional(kwargs):

    @property
    def as_json(self):
        dict = {}
        for required in REQUIRED and not required in RESTRICTED:
            dict[required] = self[required]

        for optional in OPTIONAL
            if not self[optional] is None and not optional in RESTRICTED:
                dict[optional] = self[optional]

        for restricted in RESTRICTED:
            if not self[restricted] is None:
                dict[restricted] = self[restricted].as_json

        return json.dumps(dict)

    def build_required(self, *args, **kwargs):
        for required in REQUIRED:
            self[required] = kwargs[required]

    def build_optional(self, *args, **kwargs):
        for optional in OPTIONAL
            if optional in kwargs:
                self[optional] = kwargs[optional]
            else:
                self[optional] = None

    def send(self):
        url = uri + self.ENDPOINT
        requests.post(url, self.as_json)

class SendMessage(BaseMethod):

    ENDPOINT = '/sendMessage'

    RESTRICTED = [
        'reply_markup'
    ]

    REQUIRED = [
        'chat_id',
        'text'
    ]

    OPTIONAL = [
        'parse_mode',
        'parse_mode',
        'disable_web_page_preview',
        'disable_notification',
        'reply_to_message_id',
        'reply_markup'
    ]

class ForwardMessage(BaseMethod):

    ENDPOINT = '/forwardMessage'

    REQUIRED = [
        'chat_id',
        'from_chat_id',
        'message_id'
    ]

    OPTIONAL = [
        'disable_notification'
   ]

class SendPhoto(BaseMethod):

    ENDPOINT = '/sendPhoto'

    RESTRICTED = [
        'reply_markup'
    ]

    REQUIRED = [
        'chat_id',
        'photo'
    ]

    OPTIONAL = [
        'caption',
        'parse_mode',
        'disable_notification',
        'reply_to_message_id',
        'reply_markup'
    ]

class SendAudio(BaseMethod):

    ENDPOINT = '/sendAudio'

    RESTRICTED = [
        'reply_markup'
    ]

    REQUIRED = [
        'chat_id',
        'audio'
    ]

    OPTIONAL = [
        'caption',
        'parse_mode',
        'duration',
        'performer',
        'title',
        'disable_notification',
        'reply_to_message_id',
        'reply_markup'
    ]
