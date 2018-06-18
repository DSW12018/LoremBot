import json
from .base import Base


class ReplyKeyboardMarkup(Base):

    REQUIRED = [
        'keyboard'
    ]
    OPTIONAL = [
        'resize_keyboard',
        'one_time_keyboard',
        'selective'
    ]

    @property
    def as_json(self):
        dict = {
            "keyboard": self.keyboard_as_dict,
            "resize_keyboard": self.resize_keyboard,
            "one_time_keyboard": self.one_time_keyboard,
            "selective": self.selective
        }
        return json.dumps(dict)

    @property
    def keyboard_as_dict(self):
        return [keyboard.__dict__ for keyboard in self.keyboard]
