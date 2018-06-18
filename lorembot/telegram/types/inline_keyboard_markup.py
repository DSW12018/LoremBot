import json
from .base import Base


class InlineKeyboardMarkup(Base):

    REQUIRED = [
        'inline_keyboard'
    ]

    @property
    def as_json(self):
        dict = {
            "inline_keyboard": self.inline_keyboard_as_dict
        }
        return json.dumps(dict)

    @property
    def inline_keyboard_as_dict(self):
        return [
            inline_keyboard.__dict__ for inline_keyboard in self.inline_keyboard
        ]
