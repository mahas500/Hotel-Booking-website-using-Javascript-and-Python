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