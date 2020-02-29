import uuid
from wsgiref import headers

from flask import session, jsonify
from DAO.CustomerDAO import CustomerDAO
from Exceptions.NoCustomersExist import NoCustomersExist
from Exceptions.SomethingWentWrong import SomethingWentWrong
from Service.EmailService import EmailService
from Service.RoomService import RoomService


class CustomerService:
    customerDAO = CustomerDAO()
    emailService = EmailService()
    roomService = RoomService()

    @classmethod
    def forgotPassword(cls, data):
        otp = str(uuid.uuid4())
        OTP = otp[0:6]
        responseData = cls.customerDAO.forgotPasswordDB(data.get('customer_id'), data.get('email'),OTP)
        cls.emailService.forgotPasswordEmail(responseData.get('customer_id'), responseData.get('email'),OTP)
        return responseData


    @classmethod
    def newPassword(cls, data):
        responseData = cls.customerDAO.UpdateNewPassword(data.get('password'), data.get('OTP'))
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
            responseData = cls.customerDAO.createNewCustomer(data.get('name'), data.get('username'), data.get('password'),
                                                         data.get('email'),
                                                         data.get('contact_no'))

            cls.emailService.custCreateMail(responseData.get('customer_id'), responseData.get('email'))
        else:
            raise SomethingWentWrong
        return responseData

    @classmethod
    def customerLogin(cls, data):
        customerData = cls.customerDAO.customerLogin(data.get('customer_id'), data.get('password'))
        session['loginData'] = customerData
        responseData = cls.roomService.getAllRooms()
        session['RoomsData'] = responseData
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
    def createCustomerCheck(cls, name,username,password,email,contact_no):
        responseData = cls.customerDAO.createNewCustomer(name,username,password,email,contact_no)
        if responseData is not None:
            return True
        else:
            return False