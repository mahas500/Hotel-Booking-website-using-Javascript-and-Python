from wsgiref import headers

from flask import session

from DAO.RoomDAO import RoomDAO
from DAO.BookingDAO import BookingDAO


class RoomService:
    roomDAO = RoomDAO()
    bookingDAO = BookingDAO()

    @classmethod
    def adminLogin(cls, data):
        adminData = cls.roomDAO.adminLogin(data.get('admin_id'), data.get('password'))
        session['adminDataStored'] = adminData
        roomData = cls.getAllRooms()
        session['RoomsDataAdmin'] = roomData
        responseData=cls.getAllBookingsfromDB()
        session['BookingsDataAdmin'] = responseData
        return responseData


    @classmethod
    def getAllBookingsfromDB(cls):
        responseData = cls.bookingDAO.getAllBookings()
        return responseData


    @classmethod
    def getAllRooms(cls):
        responseData = cls.roomDAO.getAllRooms()
        return responseData


    @classmethod
    def addRoom(cls, data):
        responseData = cls.roomDAO.addNewRoom(data.get('room_number'), data.get('price'), data.get('ratingOutofTen'))
        return responseData

    @classmethod
    def deleteRoom(cls, data):
        cls.roomDAO.deleteRoomFromDB(data.get('room_id'))
        return None

    @classmethod
    def checkRoomIsAvailable(cls, data):
        responseData = cls.roomDAO.checkRoomIsAvailable(data)
        if responseData is not None:
            return True
        else:
            return None
