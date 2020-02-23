import smtplib
import ssl
from flask_mail import Mail, Message
from app import mail


class EmailService:

    @classmethod
    def sendEmail(cls,data):
        msg = Message('Room booking confirmation mail!!!', sender='mahashabdemanik@gmail.com',
                      recipients=[data])
        msg.body = "Hi " \
                   "Your Room has been booked successfully. We hope you have a great stay. " \
                   "Thanks," \
                   "Admin"
        msg.html = "This is <h1>Hello All HTML</h1>"
        mail.send(msg)
        return "Mail sent successfully!"