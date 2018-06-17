import json
from .type_base import TypeBase


class ReplyKeyboardMarkup(TypeBase):

    def __init__(self, *args, **kwargs):
        self.keyboard = kwargs['keyboard']
        self.resize_keyboard = kwargs['resize_keyboard']
        self.one_time_keyboard = kwargs['one_time_keyboard']
        self.selective = kwargs['selective']


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
