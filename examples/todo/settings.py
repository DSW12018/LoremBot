from lorembot.utils import CommandMapper
from lorembot.settings import Settings
from commands import TaskCommandsCollection

# The commands of your chatbot
COMMANDS = [
    CommandMapper('start', TaskCommandsCollection.start),
    CommandMapper('list', TaskCommandsCollection.list)
]

TOKEN = ""

settings = Settings(
    token=TOKEN,
    commands=COMMANDS,
    interval=0.5,
    timeout=100
)
