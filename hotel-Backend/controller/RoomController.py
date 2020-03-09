import json
import os
import base64
from flask import request, render_template, url_for
from flask import session
from werkzeug.utils import secure_filename, redirect
from DAO.RoomDAO import RoomDAO
from CustomUtils import CustomUtils
from Exceptions.NoBookingsExist import NoBookingsExist
from Exceptions.NotAuthorized import NotAuthorized
from Exceptions.RoomNotAvailable import RoomNotAvailable
from Exceptions.RoomWithGivenIdDoesNotExist import RoomWithGivenIdDoesNotExist
from Exceptions.RoomWithGivenNumberAlreadyExist import RoomWithGivenNumberAlreadyExist
from Exceptions.WrongCredentials import WrongCredentials
from Service.RoomService import RoomService
from app import app
from DAO.BookingDAO import BookingDAO

roomService = RoomService()
roomDAO = RoomDAO()
bookingDAO = BookingDAO()

@app.route("/adminLogin", methods=['POST'])
def adminLogin():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = roomService.adminLogin(request.json)


        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except NoBookingsExist:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.NO_BOOKINGS_EXIST
    except RoomNotAvailable:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.ROOM_NOT_AVAILABLE
    except WrongCredentials:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.WRONG_CREDENTIALS
    return wsResponse


@app.route("/addRoomPage", methods=['GET'])
def addRoomPage():
    return render_template('addRoomPage.html')


@app.route('/deleteRoom', methods=['POST'])
def deleteRoom():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = roomService.deleteRoom(request.headers, request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except RoomWithGivenIdDoesNotExist:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.ROOM_WITH_GIVEN_ID_DOES_NOT_EXIST
    except NotAuthorized:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.NOT_AUTHORIZED
    return wsResponse


@app.route("/changeRoomStatus", methods=['POST'])
def changeRoomStatus():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = roomService.changeRoomStatus(request.headers, request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except RoomWithGivenNumberAlreadyExist:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.ROOM_WITH_GIVEN_NUMBER_ALREADY_EXIST
    except NotAuthorized:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.NOT_AUTHORIZED
    return wsResponse


@app.route('/deleteRoomPage', methods=['GET'])
def deleteRoomPage():
    return render_template('deleteRoomPage.html')


@app.route("/adminLoginPage", methods=['GET'])
def adminLoginPage():
    return render_template('adminLoginPage.html')


@app.route("/adminDashboard", methods=['GET'])
def adminDashboard():
    global decodedImage
    allData = roomDAO.getAllRoomsForAdmin()
    responseData = roomDAO.getAllRooms()
    items = []

    for i in allData:
        for key, value in i.items():
            if key == 'image':
                decodedImage = value.decode("utf-8")
                items.append({key: decodedImage})

    responseData = responseData + items
    return render_template('adminDashboardMainContent.html', response=responseData)


@app.route('/adminLogoutPage', methods=['GET'])
def adminLogoutPage():
    global x
    for key, value in session['adminDataStored'].items():
        if key == 'admin_id':
            x = value
            break
    roomService.adminLogoutService(x)
    return render_template('adminLogoutPage.html')


@app.route('/addRoomFromtheForm', methods=['POST'])
def addRoomFromtheForm():
    global decodedImage
    file = request.files['file']
    room_number = request.form['number']
    price = request.form['roomprice']
    Average_Rating = request.form['ratings']
    facilities = request.form['facility']

    image_string = file.read()
    image = base64.b64encode(image_string)

    responseData = roomService.addRoom(room_number, price, Average_Rating, facilities,image)

    return render_template('addRoomFromForm.html')


@app.route('/addRoomFromForm')
def addRoomFromForm():
    return render_template('addRoomFromForm.html')


@app.route('/RoomBookingPage')
def RoomBookingPage():
    responseBookingData = bookingDAO.getAllBookings()
    session['BookingsDataAdmin'] = responseBookingData
    return render_template('RoomBookingPage.html')


@app.route('/CustomerEnquiries')
def CustomerEnquiries():
    incidentData = roomDAO.Customerincident()
    session['CustomerIncidents'] = incidentData
    enquiryData = roomDAO.CustomerEnquiry()
    session['NewCustomerEnquiry'] = enquiryData
    return render_template('CustomerEnquiries.html')