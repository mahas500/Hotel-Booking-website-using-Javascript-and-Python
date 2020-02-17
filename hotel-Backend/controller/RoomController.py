from app import app
from flask import jsonify
from flask import flash, request

from Service.RoomService import RoomService

roomService = RoomService()

@app.route("/getRooms", methods=['GET'])
def getRooms():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = roomService.getAllRooms()
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse


@app.route("/addRoom", methods=['POST'])
def addRoom():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = roomService.addRoom(request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse


@app.route('/deleteRoom', methods=['POST'])
def deleteRoom():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = roomService.deleteRoom(request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse

