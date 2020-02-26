from app import app
import urllib.parse
import json
from flask import jsonify, redirect, url_for, session
from flask import flash, request, render_template

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
    if request.method == 'POST':
        jsonData = request.json
        responseData=customerService.customerLogin(jsonData)
        session['loginData']=responseData
        return responseData


@app.route("/userLoginPage", methods=['GET'])
def userLoginPage():
    return render_template('UserLogin.html')


@app.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template('dashboard.html')


@app.route("/registerUser", methods=['GET'])
def registerUser():
    return render_template('registerUser.html')