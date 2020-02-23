import smtplib
import ssl


class EmailService:
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "mahashabdemanik@gmail.com"
    password = "evrdwyscgmtllqad"
    context = ssl.create_default_context()
    Subject = "Room booking confirmation mail!!!"
    message = "Your Room has been booked successfully. We hope you have a great stay"

    @classmethod
    def sendEmail(cls, receiver_email):
        try:
            print(receiver_email)
            #print(cls.message, receiver_email, cls.Subject)

            with smtplib.SMTP(cls.smtp_server, cls.port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=cls.context)
                server.ehlo()  # Can be omitted
                server.login(cls.sender_email, cls.password)
                server.sendmail(cls.sender_email, cls.Subject, receiver_email, cls.message)
            return True
        except Exception as e:
            return False
