class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}")


emails = []
command = input()
while not command == "Stop":
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

index_emails = [int(el) for el in input().split(", ")]
for i in index_emails:
    emails[i].send()

for mails in emails:
    mails.get_info()

