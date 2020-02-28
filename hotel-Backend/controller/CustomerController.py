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


@app.route("/forgotPasswordForm", methods=['GET'])
def forgotPasswordForm():
    return render_template('forgotPasswordForm.html')


@app.route("/forgotPassword", methods=['POST'])
def forgotPassword():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = customerService.forgotPassword(request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse


@app.route("/newPassword", methods=['POST'])
def newPassword():
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = customerService.newPassword(request.json)
    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1
    return wsResponse


@app.route("/passwordChangedPage",methods=['GET'])
def passwordChangedPage():
    return render_template('passwordChangedForm.html')


@app.route("/addOTP", methods=['GET'])
def addOTP():
    return render_template('addOTP.html')


@app.route("/addCustomerInDB", methods=['POST'])
def addCustomerInDB():
    if request.method == 'POST':
        wsResponse = {"resultSet": None, "operationStatus": None}
        responseData = customerService.createCustomer(request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
        return wsResponse


@app.route("/customerLogin", methods=['POST'])
def customerLogin():
    if request.method == 'POST':
        wsResponse = {"resultSet": None, "operationStatus": None}
        responseData=customerService.customerLogin(request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
        return wsResponse



@app.route("/userLoginPage", methods=['GET'])
def userLoginPage():
    return render_template('UserLogin.html')



@app.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template('dashboard.html')


@app.route("/adminDashboard", methods=['GET'])
def adminDashboard():
    return render_template('adminDashboard.html')


@app.route("/registerUser", methods=['GET'])
def registerUser():
    return render_template('registerUser.html')


@app.route("/adminLoginPage", methods=['GET'])
def adminLoginPage():
    return render_template('adminLoginPage.html')