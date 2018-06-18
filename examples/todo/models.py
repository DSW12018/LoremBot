from lorembot.models import BaseModel
from sqlalchemy.types import *

class MessageData(BaseModel):
    __tablename__ = 'messagedata'

    id = Column(Integer, primary_key=True)
    chat = Column(Integer)
    name = Column(String)
    status = Column(String)


    def __repr__(self):
        return "<MessageData(id={}, chat={}, name='{}', status='{}')>".format(
            self.id, self.chat, self.name, self.status
        )
