from app import app
from flask import jsonify
from flask import flash, request,render_template
from flask_mail import Mail, Message
from app import mail

from Service.BookingService import BookingService
from Service.EmailService import EmailService

bookingService = BookingService()



@app.route("/getAllBookings", methods=['GET'])
def getAllBookings():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = bookingService.getAllBookings()
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse


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


@app.route("/contactUsViaHome", methods=['POST'])
def contactUsViaHome():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = bookingService.contactUsViaHome(request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse


@app.route("/contactUsForm")
def contactUsForm():
    return render_template('contactUsForm.html')


@app.route("/contactUsViaHomeForm")
def contactUsViaHomeForm():
    return render_template('contactUsFromHomePage.html')


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def error404(error):
    return render_template('404ErrorPage.html')


@app.errorhandler(500)
def error500(error):
    return render_template('500ErrorPage.html')


@app.errorhandler(405)
def error405(error):
    return render_template('405ErrorPage.html')


@app.errorhandler(403)
def error403(error):
    return render_template('403ErrorPage.html')


@app.errorhandler(400)
def error400(error):
    return render_template('400ErrorPage.html')


@app.errorhandler(502)
def error502(error):
    return render_template('502ErrorPage.html')