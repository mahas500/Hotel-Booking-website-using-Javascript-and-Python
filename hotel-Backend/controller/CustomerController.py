from CustomUtils import CustomUtils
from Exceptions.InvalidContactNumber import InvalidContactNumber
from Exceptions.InvalidEmail import InvalidEmail
from Exceptions.InvalidName import InvalidName
from Exceptions.NewPasswordCannotBeSameAsOldPassword import NewPasswordCannotBeSameAsOldPassword
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
from DAO.RoomDAO import RoomDAO

customerService = CustomerService()
roomDAO = RoomDAO()

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
    except NewPasswordCannotBeSameAsOldPassword:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.NEW_PASSWORD_SAME_AS_OLD_PASSWORD
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
    except InvalidContactNumber:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.INVALID_CONTACT_NUMBER
    except InvalidEmail:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.INVALID_EMAIL
    except InvalidName:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.INVALID_NAME
    except SomethingWentWrong:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG
    return wsResponse


@app.route("/customerLogin", methods=['POST'])
def customerLogin():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = customerService.customerLogin(request.json)
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
    global decodedImage
    allData = roomDAO.getAllDataForUser()
    responseData = roomDAO.getAllRoomsForUser()
    items = []

    for i in allData:
        for key, value in i.items():
            if key == 'image':
                decodedImage = value.decode("utf-8")
                items.append({key: decodedImage})

    responseData = responseData + items
    return render_template('dashboardMainContent.html', response=responseData)


@app.route("/registerUser", methods=['GET'])
def registerUser():
    return render_template('registerUser.html')


@app.route("/userLogoutPage",methods=['GET'])
def userLogoutPage():
    global x
    for key, value in session['loginData'].items():
        if key == 'customer_id':
            x = value
            break
    customerService.userLogoutService(x)
    return render_template('userLogoutPage.html')