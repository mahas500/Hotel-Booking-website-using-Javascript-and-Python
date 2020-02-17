from wsgiref import headers
from DAO.BookingDAO import BookingDAO
from Service.CustomerService import CustomerService
from Service.RoomService import RoomService

class BookingService:
    bookingDAO = BookingDAO()
    customerService=CustomerService()

    @classmethod
    def addBooking(cls,header,data):
        print("Hi booking")
        checkCustomer = cls.customerService.checkCustomerFromSessionID(header.get('session_id'))
        print(checkCustomer)
        if checkCustomer is not None:
            responseData = cls.booking.addRoomBooking(checkCustomer.get('customer_id'),data.get('room_id'))
        return responseData

