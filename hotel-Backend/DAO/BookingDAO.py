import uuid

import pymysql
import json
from dbconfig import mysql
from flask import jsonify

class BookingDAO:

    @classmethod
    def addRoomBooking(cls, customer_id, room_id):
        try:
            bookingId = str(uuid.uuid4())
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into booking (booking_id, customer_id,room_id) value (%s, %s, %s)",
                (bookingId, customer_id, room_id))
            conn.commit()
            cursor.execute("SELECT * from booking r WHERE r.booking_id = %s",
                           bookingId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

