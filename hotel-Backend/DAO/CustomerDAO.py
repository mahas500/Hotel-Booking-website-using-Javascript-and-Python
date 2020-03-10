import uuid
import pymysql
import json
from dbconfig import mysql
from flask import jsonify


class CustomerDAO:

    @classmethod
    def OTPCheck(cls, OTP):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer WHERE OTP = %s",
                           OTP)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def forgotPasswordCheck(cls, customer_id,email):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer WHERE customer_id = %s and email=%s",
                           (customer_id,email))
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


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
    def UpdateNewPassword(cls, password, OTP):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("Update customer set password = %s where OTP=%s",
                           (password,OTP))
            conn.commit()
            cursor.execute("Update customer set OTP = null where password=%s",
                           password)
            conn.commit()
            cursor.execute("select * from customer where password = %s",
                           password)

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

            cursor.execute("SELECT customer_id,name,username,email,contact_no from customer")
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
    def customerLogin(cls, username, password):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from customer where username = %s and password= %s",
                           (username, password))
            rows = cursor.fetchone()
            if rows is not None:
                sessionId = str(uuid.uuid4())
                cursor.execute("update customer set session_id = %s where username = %s",
                               (sessionId, username))
                conn.commit()

                cursor.execute("SELECT * from customer where username = %s and password= %s",
                               (username, password))
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

    @classmethod
    def getHashPass(cls, username):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT password from customer where username=%s",
                           username)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def userLogoutDAO(cls,customer_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("update customer set session_id = null where customer_id = %s",
                           customer_id)
            conn.commit()

            cursor.execute("SELECT * from customer where customer_id = %s",
                           customer_id)
            row = cursor.fetchone()
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()