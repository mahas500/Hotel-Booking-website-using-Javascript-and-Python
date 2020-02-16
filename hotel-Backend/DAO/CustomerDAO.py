import uuid

import pymysql
import json
from dbconfig import mysql
from flask import jsonify


class CustomerDAO:

    @classmethod
    def getAllCustomersfromDB(cls):

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer c")
            rows = cursor.fetchall()
            return rows
            cursor.close()
            conn.close()
