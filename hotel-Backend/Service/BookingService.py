from wsgiref import headers
from DAO.BookingDAO import BookingDAO
from DAO.CustomerDAO import CustomerDAO
from DAO.RoomDAO import RoomDAO
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
            raise SomethingWentWrong
        return responseData

    @classmethod
    def addBooking(cls, header, data):
        if cls.customerService.checkCustomerFromSessionID(header.get('session_id')):
            checkCustomer = cls.customerDAO.checkCustomerFromSessionID(header.get('session_id'))
            if cls.roomService.checkRoomIsAvailable(data.get('room_id')):
                cls.roomDAO.checkRoomIsAvailable(data.get('room_id'))
                responseData = cls.bookingDAO.addRoomBooking(checkCustomer.get('customer_id'), data.get('room_id'),
                                                             checkCustomer.get('email'))
                cls.emailService.sendEmail(checkCustomer.get('email'))
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
        if cls.contactUsViaHomeCheck(data.get('name'), data.get('email'),
                                     data.get('description')):

            responseData = cls.bookingDAO.contactUsViaHome(data.get('name'), data.get('email'),
                                                           data.get('description'))
            cls.emailService.contactUsEmailbyHome(responseData.get('query_id'), data.get('name'), data.get('email'),
                                                  data.get('description'))
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
