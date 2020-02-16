from wsgiref import headers
from DAO.CustomerDAO import CustomerDAO


class CustomerService:
    customerDAO = CustomerDAO()

    @classmethod
    def getAllCustomers(cls):
        responseData = cls.customerDAO.getAllCustomersfromDB()
        return responseData