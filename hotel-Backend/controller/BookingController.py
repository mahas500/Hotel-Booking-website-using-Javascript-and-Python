from app import app
from flask import jsonify
from flask import flash, request
from flask_mail import Mail, Message
from app import mail

from Service.BookingService import BookingService
from Service.EmailService import EmailService

bookingService = BookingService()
emailService = EmailService()


@app.route("/addBooking", methods=['POST'])
def addBooking():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = bookingService.addBooking(request.headers, request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse

@app.route("/contactUS", methods=['POST'])
def contactUS():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = bookingService.contactUS(request.headers,request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse

@app.route("/mail")
def index():
   msg = Message('Hello', sender = 'mahashabdemanik@gmail.com', recipients = ['mahamanik@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"