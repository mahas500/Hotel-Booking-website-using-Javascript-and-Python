from wsgiref import headers
from DAO.BookingDAO import BookingDAO
from DAO.CustomerDAO import CustomerDAO
from Service.CustomerService import CustomerService
from Service.RoomService import RoomService

class BookingService:
    bookingDAO = BookingDAO()
    customerService=CustomerService()
    customerDAO = CustomerDAO()
    roomService = RoomService()

    @classmethod
    def addBooking(cls,header,data):
        #print("Hi booking")
        checkCustomer = cls.customerService.checkCustomerFromSessionID(header.get('session_id'))
        checkRoomAvailibity = cls.roomService.checkRoomIsAvailable(data.get('room_id'))
        if checkRoomAvailibity is not None:
            responseData = cls.bookingDAO.addRoomBooking(checkCustomer.get('customer_id'),data.get('room_id'))
            return responseData
        else:
            return None

