import uuid

import pymysql
import json
from dbconfig import mysql
from flask import jsonify

class RoomDAO:


    @classmethod
    def adminLogin(cls, admin_id, password):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from admin where admin_id = %s and password= %s",
                           (admin_id, password))
            rows = cursor.fetchone()
            if rows is not None:
                sessionId = str(uuid.uuid4())
                cursor.execute("update admin set session_id = %s where admin_id = %s",
                               (sessionId, admin_id))
                conn.commit()

                cursor.execute("SELECT * from admin where admin_id = %s and password= %s",
                               (admin_id, password))
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
    def getAllRooms(cls):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from room where availibility='yes'")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def addNewRoom(cls, room_number, price, ratingOutofTen):
        try:
            roomId = str(uuid.uuid4())
            isAvailable='Yes'
            EuroPrice='€'
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into room (room_id, room_number,price,ratingOutofTen,availibility) value (%s, %s, %s,%s, %s)",
                (roomId, room_number, price+EuroPrice, ratingOutofTen, isAvailable))
            conn.commit()
            cursor.execute("SELECT * from room r WHERE r.room_id = %s",
                           roomId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def deleteRoomFromDB(cls, room_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("DELETE from room where room_id=%s", room_id)
            conn.commit()
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def checkRoomIsAvailable(cls, room_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from room where availibility='Yes' and room_id=%s",
                            room_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()