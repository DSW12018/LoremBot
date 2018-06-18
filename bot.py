from lorembot.services import TelegramService
from lorembot.observers import Messaging
from lorembot.utils import CommandMapper
from lorembot.settings import Settings
from lorembot.telegram.methods import SendContact, SendMessage
#from .commands import TaskCommands

from lorembot.command_collection import CommandCollection
#from models import TODO
from lorembot.telegram.methods import SendContact

class TaskCommands(CommandCollection):


    def list(message):
        buttons = [
        #    KeyboardButton(text='Adicionar Contato')
        ]
        # keyboard = KeyBoardMarkup()
        contact = {
            'chat_id': message['from']['id'],
            'phone_number': '900000000',
            'first_name': 'John Doe',
            # 'reply_markup': keyboard
        }
        CommandCollection.response(SendContact(**contact))

    def start(message):
        msg = {
            'chat_id': message['from']['id'],
            'text': "Olá " + message['from']['first_name'] + "!"
        }
        CommandCollection.response(SendMessage(**msg))

# The commands of your chatbot
COMMANDS = [
    CommandMapper('/start', TaskCommands.start),
    CommandMapper('list', TaskCommands.list)
]

TOKEN = "597378495:AAGXqZOta46LZ_7NhtqCpGp7i9JWaJ6gyV8"

settings = Settings(
    token=TOKEN,
    commands=COMMANDS,
    interval=0.5,
    timeout=100
)

def main():

    updater = TelegramService()
    messaging = Messaging()

    # Attaching obsersers to chatbot
    updater.attach(messaging)
    # updater.attach(payments)
    # updater.attach(responsing)
    updater.fetch_updates()


if __name__ == '__main__':
    main()
