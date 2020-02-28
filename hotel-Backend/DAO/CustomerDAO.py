import uuid
import pymysql
import json
from dbconfig import mysql
from flask import jsonify


class CustomerDAO:

    @classmethod
    def forgotPasswordDB(cls,customer_id,email,otp):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("update customer set otp=%s where customer_id=%s and email=%s",
                           (otp,customer_id,email))
            conn.commit()
            cursor.execute("SELECT * from customer WHERE customer_id = %s",
                           customer_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


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


    @classmethod
    def createNewCustomer(cls, name, username, password, email, contact_no):
        try:
            customerId = str(uuid.uuid4())

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into customer (customer_id, name,username,password,email,contact_no) value (%s, %s, %s,%s, %s, %s)",
                (customerId, name, username, password, email, contact_no))
            conn.commit()
            cursor.execute("SELECT * from customer WHERE customer_id = %s",
                           customerId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def customerLogin(cls, customer_id, password):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer where customer_id = %s and password= %s",
                           (customer_id, password))
            rows = cursor.fetchone()
            if rows is not None:
                sessionId = str(uuid.uuid4())
                cursor.execute("update customer set session_id = %s where customer_id = %s",
                               (sessionId, customer_id))
                conn.commit()

                cursor.execute("SELECT * from customer where customer_id = %s and password= %s",
                               (customer_id, password))
                rows = cursor.fetchone()
                return rows
            else:
                return None
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def checkCustomerFromSessionID(cls,session_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer where session_id=%s",
                           session_id)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()