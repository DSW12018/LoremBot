from .config import config


class CommandHandler():
    def match(cmd, message):
        for command in config.commands:
            if cmd == command.command:
                command.function(message)
