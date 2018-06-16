from services import SubjectTelegram
from obsersers import Messaging


def main():
    updater = SubjectTelegram()
    messaging = Messaging()

    # Attaching obsersers to chatbot
    updater.attach(messaging)
    updater.attach(payments)
    updater.attach(responsing)

    updater.fetch_updates()


if __name__ == '__main__':
    main()
