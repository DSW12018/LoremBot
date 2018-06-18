import requests
import json
from .tobject import TObject
from ..config import config

class BaseMethod(TObject):

    RESTRICTED = []

    @property
    def as_json(self):
        dict = {}
        for required in self.REQUIRED:
            if not required in self.RESTRICTED:
                dict[required] = self[required]

        for optional in self.OPTIONAL:
            if not self[optional] is None and not optional in self.RESTRICTED:
                dict[optional] = self[optional]

        for restricted in self.RESTRICTED:
            if not self[restricted] is None:
                dict[restricted] = self[restricted].as_json

        return json.dumps(dict)

    def send(self):
        url = config.uri + self.ENDPOINT
        headers = { 'Content-Type': 'application/json' }
        requests.post(url, data=self.as_json, headers=headers)

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

class SendDocument(BaseMethod):

    ENDPOINT = '/sendDocument'

    RESTRICTED = [
        'reply_markup'
    ]

    REQUIRED = [
        'chat_id',
        'document'
    ]

    OPTIONAL = [
        'caption',
        'parse_mode',
        'disable_notification',
        'reply_to_message_id',
        'reply_markup'
    ]

class SendVideo(BaseMethod):

    ENDPOINT = '/sendVideo'

    RESTRICTED = [
        'reply_markup'
    ]

    REQUIRED = [
        'chat_id',
        'video'
    ]

    OPTIONAL = [
        'caption',
        'parse_mode',
        'supports_streaming',
        'width',
        'height',
        'duration',
        'disable_notification',
        'reply_to_message_id',
        'reply_markup'
    ]

class SendVoice(BaseMethod):

    ENDPOINT = '/sendVoice'

    RESTRICTED = [
        'reply_markup'
    ]

    REQUIRED = [
        'chat_id',
        'voice'
    ]

    OPTIONAL = [
        'caption',
        'parse_mode',
        'duration',
        'disable_notification',
        'reply_to_message_id',
        'reply_markup'
    ]

class SendVideoNote(BaseMethod):

    ENDPOINT = '/sendVideoNote'

    RESTRICTED = [
        'reply_markup'
    ]

    REQUIRED = [
        'chat_id',
        'video_note'
    ]

    OPTIONAL = [
        'duration',
        'length',
        'disable_notification',
        'reply_to_message_id',
        'reply_markup'
    ]

class SendLocation(BaseMethod):

    ENDPOINT = '/sendLocation'

    RESTRICTED = [
        'reply_markup'
    ]

    REQUIRED = [
        'chat_id',
        'location',
        'latitude',
        'longitude'
    ]

    OPTIONAL = [
        'live_period',
        'disable_notification',
        'reply_to_message_id',
        'reply_markup'
    ]

class SendContact(BaseMethod):

    ENDPOINT = '/sendContact'

    RESTRICTED = [
        'reply_markup'
    ]

    REQUIRED = [
        'chat_id',
        'phone_number',
        'first_name'
    ]

    OPTIONAL = [
        'last_name',
        'disable_notification',
        'reply_to_message_id',
        'reply_markup'
    ]
