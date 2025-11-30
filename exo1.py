#Violations in the original class

#model 
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
#user management
class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
#DATAbE 
class DatabaseService:
    def save(self, user):
        print(f"Saving {user.name} to database...")
#EMAIL
class EmailService:
    def send_welcome_email(self, user):
        print(f"Sending welcome email to {user.email}")
#REPORTING
class ReportService:
    def generate(self, users):
        print("Generating report for users:", [u.name for u in users])
