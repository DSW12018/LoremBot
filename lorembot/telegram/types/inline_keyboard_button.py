from .base import Base


class InlineKeyboardButton(Base):

    REQUIRED = [
        'text'
    ]

    OPTIONAL = [
        'url',
        'callback_data',
        'switch_inline_query',
        'switch_inline_query_current_chat',
        'callback_game',
        'pay'
    ]
