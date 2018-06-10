import json
import psycopg2
from myapi.api.database.config import config
from psycopg2.extras import RealDictCursor
from flask_bcrypt import Bcrypt


def add_user(data):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("INSERT INTO USERS (firstname,lastname, username, role, password) values(%s,%s,%s,%s,%s)",
                    (
                        data['firstname'],
                        data['lastname'],
                        data['username'],
                        data['role'],
                        data['password'])
                    )

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        if conn is not None:
            conn.close()


def login(username):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username = %s", [username])

        data = cur.fetchone()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        if conn is not None:
            conn.close()


def add_request(data):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("INSERT INTO requests (username, title, request, status) values( %s, %s, %s, %s)",
                    (
                        data['username'],
                        data['title'],
                        data['request'],
                        data['status'])
                    )

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        if conn is not None:
            conn.close()

def allrequests(username):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM requests WHERE username = %s", [username])

        data = cur.fetchall()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        if conn is not None:
            conn.close()

def get_request_id(id, username):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM requests WHERE id = %s AND username = %s", [id, username])

        data = cur.fetchone()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        if conn is not None:
            conn.close()

def adminrequests():

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM requests")

        data = cur.fetchall()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        if conn is not None:
            conn.close()

def adminApproveDisapprove():

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(""" UPDATE requests
                SET status = %s
                WHERE id = %s""")

        data = cur.fetchone()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        if conn is not None:
            conn.close()

