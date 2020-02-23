from app import app
from flask import jsonify
from flask import flash, request

from Service.BookingService import BookingService

bookingService = BookingService()


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