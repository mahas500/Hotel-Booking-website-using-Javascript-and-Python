import os
import base64
from flask import request, render_template
from flask import session
from werkzeug.utils import secure_filename

from CustomUtils import CustomUtils
from Exceptions.NoBookingsExist import NoBookingsExist
from Exceptions.NotAuthorized import NotAuthorized
from Exceptions.RoomNotAvailable import RoomNotAvailable
from Exceptions.RoomWithGivenIdDoesNotExist import RoomWithGivenIdDoesNotExist
from Exceptions.RoomWithGivenNumberAlreadyExist import RoomWithGivenNumberAlreadyExist
from Exceptions.WrongCredentials import WrongCredentials
from Service.RoomService import RoomService
from app import app

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


@app.route("/changeRoomStatus", methods=['POST'])
def changeRoomStatus():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = roomService.changeRoomStatus(request.headers,request.json)
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


@app.route('/addRoomFromtheForm', methods=['POST'])
def addRoomFromtheForm():
    file = request.files['file']
    room_number = request.form['number']
    price = request.form['roomprice']
    Average_Rating = request.form['ratings']
    facilities = request.form['facility']

    image_string = file.read()
    image = base64.b64encode(image_string)
    dictlist=[]
    responseData = roomService.addRoom(image,room_number,price,Average_Rating,facilities)
    decodedImage = responseData.get('image').decode("utf-8")

    for key, value in responseData.items():
        temp = [key, value]
        dictlist.append(temp)
    print(dictlist)

  #  with open("F:\GitHub\Web-Development-CA\hotel-Backend\static\images\Old1.jpg", "wb") as fh:
    #    fh.write(responseData)
    #    print(fh)
    #    fh.close()
    #filename = secure_filename(file.fh)
    #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('displayImageOnPage.html',image=decodedImage,responseData=responseData)


@app.route('/addRoomFromForm')
def upload_file():
   return render_template('addRoomFromForm.html')