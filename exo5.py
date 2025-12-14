from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, user, message):
        pass

class EmailService(NotificationService):
    def send(self, user, message):
       

class SMSService(NotificationService):
    def send(self, user, message):
        

class PushService(NotificationService):
    def send(self, user, message):
       
