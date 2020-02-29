from CustomUtils import CustomUtils
from Exceptions.OTP_Not_Correct import OTP_Not_Correct
from Exceptions.WrongCredentials import WrongCredentials
from Exceptions.NoCustomersExist import NoCustomersExist
from Exceptions.RoomNotAvailable import RoomNotAvailable
from Exceptions.SomethingWentWrong import SomethingWentWrong
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
    try:
        responseData = customerService.getAllCustomers()
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except NoCustomersExist:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.NO_CUSTOMERS_EXIST
    return wsResponse


@app.route("/forgotPasswordForm", methods=['GET'])
def forgotPasswordForm():
    return render_template('forgotPasswordForm.html')


@app.route("/forgotPassword", methods=['POST'])
def forgotPassword():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = customerService.forgotPassword(request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except WrongCredentials:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.WRONG_CREDENTIALS
    return wsResponse


@app.route("/newPassword", methods=['POST'])
def newPassword():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = customerService.newPassword(request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except OTP_Not_Correct:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.OTP_NOT_CORRECT
    return wsResponse


@app.route("/passwordChangedPage",methods=['GET'])
def passwordChangedPage():
    return render_template('passwordChangedForm.html')


@app.route("/addOTP", methods=['GET'])
def addOTP():
    return render_template('addOTP.html')


@app.route("/addCustomerInDB", methods=['POST'])
def addCustomerInDB():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = customerService.createCustomer(request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except SomethingWentWrong:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG
    return wsResponse


@app.route("/customerLogin", methods=['POST'])
def customerLogin():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = customerService.customerLogin(request.json)
        print(responseData)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except RoomNotAvailable:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.ROOM_NOT_AVAILABLE
    except WrongCredentials:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.WRONG_CREDENTIALS
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