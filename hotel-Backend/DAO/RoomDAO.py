import uuid

import pymysql
import json
from dbconfig import mysql
from flask import jsonify

class RoomDAO:

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
            isAvailable='Yes';
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into room (room_id, room_number,price,ratingOutofTen,availibility) value (%s, %s, %s,%s, %s)",
                (roomId, room_number, price, ratingOutofTen, isAvailable))
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