from services import TelegramService
from obsersers import Messaging
from settings import settings

def main():
    updater = SubjectTelegram(settings)
    messaging = Messaging()

    # Attaching obsersers to chatbot
    updater.attach(messaging)
    updater.attach(payments)
    updater.attach(responsing)

    updater.fetch_updates()


if __name__ == '__main__':
    main()
