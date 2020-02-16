import uuid

import pymysql
import json
from dbconfig import mysql
from flask import jsonify


class CustomerDAO:

    @classmethod
    def getAllCustomersfromDB(cls):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()