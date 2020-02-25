
from app import app
from flask import jsonify, redirect, url_for
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
    if request.method == 'POST':
        jsonData = request.get_json()
        #wsResponse = {"resultSet": None, "operationStatus": None}
        print(jsonData)
        #print(postData.json)
        return render_template('dashboard.html')
        #responseData = customerService.customerLogin(jsonData)
        #wsResponse['resultSet'] = responseData
        #wsResponse['operationStatus'] = 1
        #return render_template('dashboard.html',result=responseData)
        #return render_template('dashboard.html')



@app.route("/userLoginPage", methods=['GET'])
def userLoginPage():
    return render_template('UserLogin.html')



@app.route("/dashboard",methods=['GET'] )
def userdashboard():
    print("Hi")
    return render_template('dashboard.html')