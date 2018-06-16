from services import SubjectTelegram
from behaviour import Messaging


def main():
    updater = SubjectTelegram()
    messaging = Messaging()

    # Attaching behaviorals to chatbot
    updater.attach(messaging)

    updater.fetch_updates()


if __name__ == '__main__':
    main()
