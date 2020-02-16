
from app import app
from flask import jsonify
from flask import flash, request

from Service.CustomerService import CustomerService

customerService = CustomerService()


@app.route("/getCustomersFromDB", methods=['GET'])
def getCustomersFromDB():
    wsResponse = {"resultSet": None, "operationStatus": None}
    print("Hey controller")
    responseData = customerService.getAllCustomers()
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse


