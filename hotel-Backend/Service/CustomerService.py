from wsgiref import headers
from DAO.CustomerDAO import CustomerDAO


class CustomerService:
    customerDAO = CustomerDAO()

    @classmethod
    def getAllCustomers(cls):
        responseData = cls.customerDAO.getAllCustomersfromDB()
        return responseData

    @classmethod
    def createCustomer(cls,data):
        responseData = cls.customerDAO.createNewCustomer(data.get('name'),data.get('username'),data.get('password'),data.get('email'),
                                                             data.get('contact_no'))
        return responseData

    @classmethod
    def customerLogin(cls,data):
        print(data.get('username'))
        responseData = cls.customerDAO.customerLogin(data.get('username'),data.get('password'))
        return responseData

    @classmethod
    def checkCustomerFromSessionID(cls,headerData):
        responseData = cls.customerDAO.checkCustomerFromSessionID(headerData)

        if responseData is not None:
            return responseData
        else:
            return False




