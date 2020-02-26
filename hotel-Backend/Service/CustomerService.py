from wsgiref import headers
from DAO.CustomerDAO import CustomerDAO
from Service.EmailService import EmailService

class CustomerService:
    customerDAO = CustomerDAO()
    emailService = EmailService()

    @classmethod
    def getAllCustomers(cls):
        responseData = cls.customerDAO.getAllCustomersfromDB()
        return responseData

    @classmethod
    def createCustomer(cls,data):
        responseData = cls.customerDAO.createNewCustomer(data.get('name'),data.get('username'),data.get('password'),data.get('email'),
                                                             data.get('contact_no'))

        cls.emailService.custCreateMail(responseData.get('customer_id'),responseData.get('email'))
        return responseData

    @classmethod
    def customerLogin(cls,data):
        responseData = cls.customerDAO.customerLogin(data.get('customer_id'),data.get('password'))
        return responseData

    @classmethod
    def checkCustomerFromSessionID(cls,headerData):
        responseData = cls.customerDAO.checkCustomerFromSessionID(headerData)

        if responseData is not None:
            return responseData
        else:
            return False




