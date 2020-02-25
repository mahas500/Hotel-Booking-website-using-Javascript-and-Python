from app import app
from flask import jsonify
from flask import flash, request,render_template
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

@app.route("/")
def index():
    return render_template('index.html')

