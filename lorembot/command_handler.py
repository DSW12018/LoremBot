from .config import config


class CommandHandler():
    def match(cmd):
        for command in config.commands:
            if cmd == command.command:
                command.function()
