from wsgiref import headers
from DAO.RoomDAO import RoomDAO


class RoomService:
    roomDAO = RoomDAO()

    @classmethod
    def getAllRooms(cls):
        responseData = cls.roomDAO.getAllRooms()
        return responseData

    @classmethod
    def addRoom(cls,data):
        responseData = cls.roomDAO.addNewRoom(data.get('room_number'),data.get('price'),data.get('ratingOutofTen'))
        return responseData

    @classmethod
    def deleteRoom(cls, data):
        cls.roomDAO.deleteRoomFromDB(data.get('room_id'))
        return None

    @classmethod
    def checkRoomIsAvailable(cls, data):
        responseData=cls.roomDAO.checkRoomIsAvailable(data)
        if responseData is not None:
            return responseData
        else:
            return None