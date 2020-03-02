import uuid
from wsgiref import headers

from flask import session, jsonify
from DAO.CustomerDAO import CustomerDAO
from DAO.RoomDAO import RoomDAO
from Exceptions.OTP_Not_Correct import OTP_Not_Correct
from Exceptions.WrongCredentials import WrongCredentials
from Exceptions.NoCustomersExist import NoCustomersExist
from Exceptions.RoomNotAvailable import RoomNotAvailable
from Exceptions.SomethingWentWrong import SomethingWentWrong
from Service.EmailService import EmailService
from Service.RoomService import RoomService


class CustomerService:
    customerDAO = CustomerDAO()
    emailService = EmailService()
    roomService = RoomService()
    roomDAO = RoomDAO()

    @classmethod
    def forgotPassword(cls, data):
        if cls.forgotPasswordCheck(data):
            otp = str(uuid.uuid4())
            OTP = otp[0:6]
            responseData = cls.customerDAO.forgotPasswordDB(data.get('customer_id'), data.get('email'), OTP)
            cls.emailService.forgotPasswordEmail(responseData.get('customer_id'), responseData.get('email'), OTP)
        else:
            raise WrongCredentials
        return responseData

    @classmethod
    def newPassword(cls, data):
        if cls.OTPCheck(data):
            responseData = cls.customerDAO.UpdateNewPassword(data.get('password'), data.get('OTP'))
        else:
            raise OTP_Not_Correct
        return responseData

    @classmethod
    def getAllCustomers(cls):
        if cls.getAllCustomersCheck():
            responseData = cls.customerDAO.getAllCustomersfromDB()
        else:
            raise NoCustomersExist
        return responseData

    @classmethod
    def createCustomer(cls, data):
        if cls.createCustomerCheck(data.get('name'), data.get('username'), data.get('password'),
                                   data.get('email'),
                                   data.get('contact_no')):
            responseData = cls.customerDAO.createNewCustomer(data.get('name'), data.get('username'),
                                                             data.get('password'),
                                                             data.get('email'),
                                                             data.get('contact_no'))

            cls.emailService.custCreateMail(responseData.get('customer_id'), responseData.get('email'))
        else:
            raise SomethingWentWrong
        return responseData

    @classmethod
    def customerLogin(cls, data):
        if cls.customerLoginCheck(data.get('customer_id'), data.get('password')):
            customerData = cls.customerDAO.customerLogin(data.get('customer_id'), data.get('password'))
            session['loginData'] = customerData
            if cls.roomService.getAllRooms():
                responseData = cls.roomDAO.getAllRooms()
                session['RoomsData'] = responseData
            else:
                raise RoomNotAvailable
        else:
            raise WrongCredentials

        return responseData

    @classmethod
    def checkCustomerFromSessionID(cls, headerData):
        responseData = cls.customerDAO.checkCustomerFromSessionID(headerData)

        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def getAllCustomersCheck(cls):
        responseData = cls.customerDAO.getAllCustomersfromDB()
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def createCustomerCheck(cls, name, username, password, email, contact_no):
        responseData = cls.customerDAO.createNewCustomer(name, username, password, email, contact_no)
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def customerLoginCheck(cls, customer_id, password):
        responseData = cls.customerDAO.customerLogin(customer_id, password)
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def forgotPasswordCheck(cls, data):
        responseData = cls.customerDAO.forgotPasswordCheck(data.get('customer_id'), data.get('email'))
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def OTPCheck(cls, data):
        responseData = cls.customerDAO.OTPCheck(data.get('OTP'))
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def userLogoutService(cls, customer_id):
        responseData = cls.customerDAO.userLogoutDAO(customer_id)
        session.pop('loginData')
        session.pop('RoomsData')
        session.pop('currentRoomData')
        return responseData
