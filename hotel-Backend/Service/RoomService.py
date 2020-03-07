import base64
from wsgiref import headers
import json
from flask import session
from werkzeug.wrappers import json

from DAO.RoomDAO import RoomDAO
from DAO.BookingDAO import BookingDAO
from Exceptions.NoBookingsExist import NoBookingsExist
from Exceptions.NotAuthorized import NotAuthorized
from Exceptions.RoomNotAvailable import RoomNotAvailable
from Exceptions.RoomWithGivenIdDoesNotExist import RoomWithGivenIdDoesNotExist
from Exceptions.RoomWithGivenNumberAlreadyExist import RoomWithGivenNumberAlreadyExist
from Exceptions.WrongCredentials import WrongCredentials


class RoomService:
    roomDAO = RoomDAO()
    bookingDAO = BookingDAO()

    @classmethod
    def adminLogin(cls, data):
        if cls.adminLoginCheck(data):
            adminData = cls.roomDAO.adminLogin(data.get('admin_id'), data.get('password'))
            session['adminDataStored'] = adminData
            if cls.getAllBookingsfromDBCheck():
                responseBookingData = cls.bookingDAO.getAllBookings()
                session['BookingsDataAdmin'] = responseBookingData
                if cls.getAllRooms():
                    responseData = cls.roomDAO.getAllRoomsForAdmin()
                else:
                    raise NoBookingsExist
            else:
                raise RoomNotAvailable
        else:
            raise WrongCredentials
        return responseData


    @classmethod
    def getAllBookingsfromDBCheck(cls):
        responseData = cls.bookingDAO.getAllBookings()
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def getAllRooms(cls):
        responseData = cls.roomDAO.getAllRooms()
        session['RoomsDataAdmin'] = responseData
        if responseData is not None:
            return True
        else:
            return False


 #   @classmethod
 #   def addRoom(cls, header,data):
  #      if cls.adminCheckFromSessionID(header):
  #          if cls.checkRoomWithNumber(data):
    #            responseData = cls.roomDAO.addNewRoom(data.get('room_number'), data.get('price'), data.get('Average_Rating'),data.get('facilities'))
  #          else:
   #             raise RoomWithGivenNumberAlreadyExist
  #      else:
 #           raise NotAuthorized
  #      return responseData


    @classmethod
    def addRoom(cls, image,room_number,price,Average_Rating,facilities):

        if cls.checkRoomWithNumber(room_number):
            responseData = cls.roomDAO.addNewRoom(room_number, price, Average_Rating,facilities,image)
            print(type(responseData))
        else:
            raise RoomWithGivenNumberAlreadyExist
        return responseData


    @classmethod
    def deleteRoom(cls,header, data):
        if cls.adminCheckFromSessionID(header):
            if cls.checkRoomWithGivenID(data):
                responseData = cls.roomDAO.deleteRoomFromDB(data.get('room_id'))
            else:
                raise RoomWithGivenIdDoesNotExist
        else:
            raise NotAuthorized
        return responseData


    @classmethod
    def changeRoomStatus(cls,header, data):
        if cls.adminCheckFromSessionID(header):
            if cls.checkRoomWithGivenID(data):
                roomDataWithGivenID = cls.roomDAO.checkRoomWithGivenID(data.get('room_id'))
                print(roomDataWithGivenID)
                checkStatus = roomDataWithGivenID.get('availibility')
                if checkStatus == 'Yes':
                    responseData = cls.roomDAO.changeStatusToNo(data.get('room_id'))
                    print(responseData)
                else:
                    responseData = cls.roomDAO.changeStatusToYes(data.get('room_id'))
                    print(responseData)
            else:
                raise RoomWithGivenIdDoesNotExist
        else:
            raise NotAuthorized
        return responseData


    @classmethod
    def checkRoomIsAvailable(cls, data):
        responseData = cls.roomDAO.checkRoomIsAvailable(data)
        if responseData is not None:
            return True
        else:
            return None


    @classmethod
    def adminLoginCheck(cls, data):
        responseData = cls.roomDAO.adminLogin(data.get('admin_id'), data.get('password'))
        if responseData is not None:
            return True
        else:
            return None

    @classmethod
    def adminCheckFromSessionID(cls, header):
        responseData = cls.roomDAO.adminCheckFromSessionID(header.get('session_id'))
        if responseData is not None:
            return True
        else:
            return None


    @classmethod
    def checkRoomWithNumber(cls, room_number):
        responseData = cls.roomDAO.checkRoomWithNumber(room_number)
        if responseData is None:
            return True
        else:
            return None


    @classmethod
    def checkRoomWithGivenID(cls, data):
        responseData = cls.roomDAO.checkRoomWithGivenID(data.get('room_id'))
        if responseData is not None:
            return True
        else:
            return None

    @classmethod
    def adminLogoutService(cls, admin_id):
        responseData = cls.roomDAO.adminLogoutDAO(admin_id)
        session.pop('adminDataStored')
        session.pop('RoomsDataAdmin')
        session.pop('BookingsDataAdmin')
        return responseData

    @classmethod
    def getCurrentRoomData(cls,room_id):
        responseData = cls.roomDAO.getCurrentRoomData(room_id)
        return responseData


    @classmethod
    def addRoomFromtheForm(cls, image_id):
        response = cls.roomDAO.addRoomFromtheForm(image_id)
        #decodedImage = base64.b64decode(response)
        #decodedImage = json.loads(json.dumps(response))
        decodedImage = base64.b64decode(response.get('image_id'))
        return decodedImage
