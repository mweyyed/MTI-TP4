 class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
 
class DatabaseService:
    def save(self, user):
        print(f"Saving {user.name} to database...")

class EmailService:
    def send_welcome_email(self, user):
        print(f"Sending welcome email to {user.email}")

class ReportService:
    def generate(self, users):
        print("Generating report for users:", [u.name for u in users])
