
from app import app

from flask import jsonify
from flask import flash, request

from Service.CustomerService import CustomerService

customerService = CustomerService()

@app.route('/getAllCustomers', methods=['GET'])
def getAllCustomers():
    wsResponse = {"resultSet": None, "operationStatus": None}

    responseData = customerService.getAllCustomers()
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1

    return wsResponse