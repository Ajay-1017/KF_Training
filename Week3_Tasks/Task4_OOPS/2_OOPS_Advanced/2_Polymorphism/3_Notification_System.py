# 3) Build a Notification System

# What to do

# Create a common parent class:
# Notification

# Create child classes:
# Email
# SMS
# WhatsApp

# Requirements:

# Each notification type should send its message differently.
# Use the same method name in every class.
# Display where the notification was sent.


class Notification:
    def Notication_isfrom(self):
        pass
    def display_message(self):
        pass

class Email(Notification):
    def Notication_isfrom(self):
        return "Notification sent via Email"
    def display_message(self):
        return "hi"
class SMS(Notification):
    def Notication_isfrom(self):
        return "Notification sent via SMS"
    def display_message(self):
        return "hello"

class WhatsApp(Notification):
    def Notication_isfrom(self):
        return "Notification sent via WhatsApp."
    def display_message(self):
        return "heyy"
 
e = Email()
s = SMS()
w = WhatsApp()
print(e.Notication_isfrom())
print(w.Notication_isfrom())
print(s.display_message())
