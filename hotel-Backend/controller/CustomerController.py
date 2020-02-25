
from app import app
from flask import jsonify
from flask import flash, request,render_template

from Service.CustomerService import CustomerService

customerService = CustomerService()


@app.route("/getCustomersFromDB", methods=['GET'])
def getCustomersFromDB():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = customerService.getAllCustomers()
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse


@app.route("/addCustomerInDB", methods=['POST'])
def addCustomerInDB():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = customerService.createCustomer(request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse


@app.route("/customerLogin", methods=['POST'])
def customerLogin():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = customerService.customerLogin(request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse


@app.route("/userLoginPage", methods=['GET'])
def userLoginPage():
    return render_template('UserLogin.html')