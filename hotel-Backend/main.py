from app import app
import pymysql
from dbconfig import mysql
from flask import jsonify
from flask import flash, request
from controller import CustomerController
from controller import RoomController
from controller import BookingController

if __name__ == '__main__':
    app.run()





