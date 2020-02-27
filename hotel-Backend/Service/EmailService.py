import smtplib
import ssl
from flask_mail import Mail, Message
from app import mail


class EmailService:

    @classmethod
    def sendEmail(cls, data):
        msg = Message('Room booking confirmation mail!!!', sender='mahashabdemanik@gmail.com',
                      recipients=[data])
        msg.html = "<h3 align='center'>Hello User</h3> <br> <p> Your room has been booked successfully</p><br>" \
                   "<p>Regards,<br>Team Admin</p>"
        mail.send(msg)
        return "Mail sent successfully!"

    @classmethod
    def contactUsEmail(cls, inci, desc, data):
        incident = inci
        description = desc
        msg = Message('Thanks for your email', sender='mahashabdemanik@gmail.com',
                      recipients=[data])
        msg.html = "<h3 align='center'>Hello User</h3> <br> <p> Thanks for reaching out to us." \
                   " We will get back to you shortly. Please find below <b>incident ID</b> for reference</p><br>" \
                   + incident + \
                   "<br>"\
                   "<b>Description</b>:" + description + \
                   "<p>Regards,<br>Team Admin</p>"
        mail.send(msg)
        return "Mail sent successfully!"

    @classmethod
    def custCreateMail(cls, cust_id, data):
        cust = cust_id
        msg = Message('Thanks for your email', sender='mahashabdemanik@gmail.com',
                      recipients=[data])
        msg.html = "<h3 align='center'>Hello User</h3> <br> <p> You have been registered successfully." \
                   " Please find below your customer ID</p><br>" \
                   "<b>Customer ID:<b>" + cust + \
                   "<p>Regards," \
                   "<br>Team Admin</p>"
        mail.send(msg)
        return None
