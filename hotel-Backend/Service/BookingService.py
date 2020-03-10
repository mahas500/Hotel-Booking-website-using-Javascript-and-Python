from wsgiref import headers

from flask import session

from DAO.BookingDAO import BookingDAO
from DAO.CustomerDAO import CustomerDAO
from DAO.RoomDAO import RoomDAO
from Exceptions.InvalidEmail import InvalidEmail
from Exceptions.InvalidName import InvalidName
from Exceptions.NoBookingsExist import NoBookingsExist
from Service.RoomService import RoomService
from Service.EmailService import EmailService
from Service.CustomerService import CustomerService
from Exceptions.SomethingWentWrong import SomethingWentWrong
from Exceptions.CustomerNotLoggedIn import CustomerNotLoggedIn
from Exceptions.RoomNotAvailable import RoomNotAvailable


class BookingService:
    bookingDAO = BookingDAO()
    customerService = CustomerService()
    customerDAO = CustomerDAO()
    roomService = RoomService()
    emailService = EmailService()
    roomDAO = RoomDAO()

    @classmethod
    def getAllBookings(cls):
        if cls.getAllBookingsData():
            responseData = cls.bookingDAO.getAllBookings()
        else:
            raise NoBookingsExist
        return responseData

    @classmethod
    def addBooking(cls, header, data):
        if cls.customerService.checkCustomerFromSessionID(header.get('session_id')):
            checkCustomer = cls.customerDAO.checkCustomerFromSessionID(header.get('session_id'))
            if cls.roomService.checkRoomIsAvailable(data.get('room_id')):
                roomData = cls.roomDAO.checkRoomIsAvailable(data.get('room_id'))
                responseData = cls.bookingDAO.addRoomBooking(checkCustomer.get('customer_id'), data.get('room_id'),
                                                             checkCustomer.get('email'))

                cls.emailService.sendEmail(checkCustomer.get('email'),responseData.get('booking_id'),
                                           roomData.get('room_number'),roomData.get('price'),roomData.get('facilities'),roomData.get('Average_Rating'))
                currentRoomData = cls.roomService.getCurrentRoomData(data.get('room_id'))
                session['currentRoomData'] = currentRoomData
            else:
                raise RoomNotAvailable
        else:
            raise CustomerNotLoggedIn
        return responseData

    @classmethod
    def contactUS(cls, header, data):
        if cls.customerService.checkCustomerFromSessionID(header.get('session_id')):
            checkCustomer = cls.customerDAO.checkCustomerFromSessionID(header.get('session_id'))
            responseData = cls.bookingDAO.contactUS(checkCustomer.get('customer_id'), checkCustomer.get('username'),
                                                    data.get('description'))
            cls.emailService.contactUsEmail(responseData.get('incident_id'), data.get('description'),
                                            checkCustomer.get('email'))
        else:
            raise CustomerNotLoggedIn
        return responseData

    @classmethod
    def contactUsViaHome(cls, data):
        if cls.contactUsViaHomeCheck(data.get('name'), data.get('email'),data.get('description')):
            z = data.get('name')
            count = 0

            for j in z:
                if j in "0, 1, 2, 3, 4, 5, 6, 7, 8, 9,@,#,$,%,&,*":
                    count = count + 1
            if count == 0:
                x = data.get('email')
                count = 0
                count1 = 0
                for i in x:
                    if i == '@':
                        count = count + 1
                    elif i == '.':
                        count1 = count1 + 1
                if count == 1 and count1 == 1:
                    responseData = cls.bookingDAO.contactUsViaHome(data.get('name'), data.get('email'),
                                                                   data.get('description'))
                    cls.emailService.contactUsEmailbyHome(responseData.get('query_id'), data.get('name'), data.get('email'),
                                                      data.get('description'))
                else:
                    raise InvalidEmail
            else:
                raise InvalidName
        else:
            raise SomethingWentWrong
        return responseData

    @classmethod
    def getAllBookingsData(cls):
        if cls.bookingDAO.getAllBookings():
            return True
        else:
            return False

    @classmethod
    def contactUsViaHomeCheck(cls, name, email, description):
        responseData = cls.bookingDAO.contactUsViaHome(name, email, description)
        if responseData is not None:
            return True
        else:
            return False
