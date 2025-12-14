from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, user, message):
        pass

class EmailService(NotificationService):
    def send(self, user, message):
        print(f"Email to {user}: {message}")

class SMSService(NotificationService):
    def send(self, user, message):
        print(f"SMS to {user}: {message}")

class PushService(NotificationService):
    def send(self, user, message):
        print(f"Push notification to {user}: {message}")

class UserNotification:
    def __init__(self, notifier: NotificationService):
        self.notifier = notifier

    def notify(self, user, message):
        self.notifier.send(user, message)

