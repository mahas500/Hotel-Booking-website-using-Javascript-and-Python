from CustomUtils import CustomUtils
from Exceptions.NoBookingsExist import NoBookingsExist
from Exceptions.NotAuthorized import NotAuthorized
from Exceptions.RoomNotAvailable import RoomNotAvailable
from Exceptions.RoomWithGivenIdDoesNotExist import RoomWithGivenIdDoesNotExist
from Exceptions.RoomWithGivenNumberAlreadyExist import RoomWithGivenNumberAlreadyExist
from Exceptions.WrongCredentials import WrongCredentials
from app import app
from flask import jsonify, session
from flask import flash, request,render_template
from Service.RoomService import RoomService

roomService = RoomService()


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



@app.route("/addRoom", methods=['POST'])
def addRoom():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        print(request.json)
        responseData = roomService.addRoom(request.headers,request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except RoomWithGivenNumberAlreadyExist:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.ROOM_WITH_GIVEN_NUMBER_ALREADY_EXIST
    except NotAuthorized:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.NOT_AUTHORIZED
    return wsResponse


@app.route("/addRoomPage", methods=['GET'])
def addRoomPage():
    return render_template('addRoomPage.html')


@app.route('/deleteRoom', methods=['POST'])
def deleteRoom():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = roomService.deleteRoom(request.headers,request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except RoomWithGivenIdDoesNotExist:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.ROOM_WITH_GIVEN_ID_DOES_NOT_EXIST
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
    return render_template('adminDashboard.html')



@app.route('/adminLogoutPage', methods=['GET'])
def adminLogoutPage():
    global x
    for key, value in session['adminDataStored'].items():
        if key == 'admin_id':
            x = value
            break
    roomService.adminLogoutService(x)
    return render_template('adminLogoutPage.html')
