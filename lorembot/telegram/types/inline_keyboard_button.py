from .base import Base


class InlineKeyboardButton(Base):

    def __init__(self, *args, **kwargs):
        self.text = kwargs['text']
        self.url = kwargs['url']
        self.callback_data = kwargs['callback_data']
        self.switch_inline_query = kwargs['switch_inline_query']
        self.switch_inline_query_current_chat = kwargs['switch_inline_query_current_chat']
        self.callback_game = kwargs['callback_game']
        self.pay = kwargs['pay']
