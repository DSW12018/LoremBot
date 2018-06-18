from .base import Base

class Chat(Base):

    REQUIRED = [
        'id',
        'type',
    ]

    OPTIONAL = [
        'title,
        'username',
        'first_name',
        'last_name',
        'all_members_are_administrators',
        'photo',
        'desciption',
        'invite_link',
        'pinned_message',
        'sticker_set_name',
        'can_set_sticker_set',
    ]
