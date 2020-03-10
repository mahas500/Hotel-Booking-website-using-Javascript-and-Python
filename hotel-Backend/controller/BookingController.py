from CustomUtils import CustomUtils
from Exceptions import NoBookingsExist
from Exceptions.CustomerNotLoggedIn import CustomerNotLoggedIn
from Exceptions.DescriptionCannotBeEmpty import DescriptionCannotBeEmpty
from Exceptions.InvalidEmail import InvalidEmail
from Exceptions.InvalidName import InvalidName
from Exceptions.NoBookingsExist import NoBookingsExist
from Exceptions.SomethingWentWrong import SomethingWentWrong
from Exceptions.RoomNotAvailable import RoomNotAvailable
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
    try:
        responseData = bookingService.getAllBookings()
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except NoBookingsExist:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.NO_BOOKINGS_EXIST
    return wsResponse


@app.route("/addBooking", methods=['POST'])
def addBooking():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = bookingService.addBooking(request.headers, request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except RoomNotAvailable:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.ROOM_NOT_AVAILABLE
    except CustomerNotLoggedIn:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.CUSTOMER_NOT_LOGGED_IN
    return wsResponse


@app.route("/RoomBookingConfirmation", methods=['GET'])
def RoomBookingConfirmation():
    return render_template('roomBookingForm.html')


@app.route("/contactUS", methods=['POST'])
def contactUS():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = bookingService.contactUS(request.headers,request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except DescriptionCannotBeEmpty:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.DESCRIPTION_EMPTY
    except CustomerNotLoggedIn:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.CUSTOMER_NOT_LOGGED_IN
    return wsResponse


@app.route("/contactUsViaHome", methods=['POST'])
def contactUsViaHome():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = bookingService.contactUsViaHome(request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except DescriptionCannotBeEmpty:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.DESCRIPTION_EMPTY
    except InvalidEmail:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.INVALID_EMAIL
    except InvalidName:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.INVALID_NAME
    except SomethingWentWrong:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG
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