from wsgiref import headers
from DAO.BookingDAO import BookingDAO
from DAO.CustomerDAO import CustomerDAO
from Service.CustomerService import CustomerService
from Service.RoomService import RoomService

class BookingService:
    bookingDAO = BookingDAO()
    customerService=CustomerService()
    customerDAO = CustomerDAO()

    @classmethod
    def addBooking(cls,header,data):
        #print("Hi booking")
        checkCustomer = cls.customerService.checkCustomerFromSessionID(header.get('session_id'))
        responseData = cls.bookingDAO.addRoomBooking(checkCustomer.get('customer_id'),data.get('room_id'))
        return responseData

