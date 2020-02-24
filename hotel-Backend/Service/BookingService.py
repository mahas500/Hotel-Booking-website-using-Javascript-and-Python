from wsgiref import headers
from DAO.BookingDAO import BookingDAO
from DAO.CustomerDAO import CustomerDAO
from Service.CustomerService import CustomerService
from Service.RoomService import RoomService
from Service.EmailService import EmailService

class BookingService:
    bookingDAO = BookingDAO()
    customerService=CustomerService()
    customerDAO = CustomerDAO()
    roomService = RoomService()
    emailService = EmailService()

    @classmethod
    def addBooking(cls,header,data):
        #print("Hi booking")
        checkCustomer = cls.customerService.checkCustomerFromSessionID(header.get('session_id'))
        checkRoomAvailibity = cls.roomService.checkRoomIsAvailable(data.get('room_id'))
        if checkRoomAvailibity is not None:
            responseData = cls.bookingDAO.addRoomBooking(checkCustomer.get('customer_id'), data.get('room_id'),
                                                         checkCustomer.get('email'))
            cls.emailService.sendEmail(checkCustomer.get('email'))
            return responseData
        else:
            return None

    @classmethod
    def contactUS(cls,header,data):
        checkCustomer = cls.customerService.checkCustomerFromSessionID(header.get('session_id'))
        responseData = cls.bookingDAO.contactUS(checkCustomer.get('customer_id'), checkCustomer.get('username'),data.get('description'))
        cls.emailService.contactUsEmail(checkCustomer.get('email'))
        return responseData

