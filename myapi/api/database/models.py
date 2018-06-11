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

        cur.execute("SELECT * FROM requests WHERE username = %s", [username])

        data = cur.fetchall()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        return ("all request issue is: ", error)
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

        data = cur.fetchall()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        return ("get request by id issue is: ", error)
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
        return ("get admin requests issue is: ", error)
    finally:
        if conn is not None:
            conn.close()


def adminApproveDisapprove(id, status):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            " UPDATE requests SET status = %s WHERE id = %s", [status, id])

        data = cur.rowcount

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return ("row updated", data)
    except (Exception, psycopg2.DatabaseError) as error:
        return ("get admin approval issue is: ", error)
    finally:
        if conn is not None:
            conn.close()


def AdminResolve(data):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            " UPDATE requests SET (id, resolve, status) values( %s, %s, %s) WHERE id = %s",
            (
                data['id'],
                data['resolve'],
                data['status']))

        data = cur.rowcount

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return ("row updated", data)
    except (Exception, psycopg2.DatabaseError) as error:
        return ("get admin resolve issue is: ", error)
    finally:
        if conn is not None:
            conn.close()


def roles(username):
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE username = %s", [username])

        data = cur.fetchone()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return data[3]
    except (Exception, psycopg2.DatabaseError) as error:
        return ("get roles in users is: ", error)
    finally:
        if conn is not None:
            conn.close()


def status(username):
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT * FROM requests WHERE username = %s", [username])

        data = cur.fetchone()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return data[4]
    except (Exception, psycopg2.DatabaseError) as error:
        return ("get status error is: ", error)
    finally:
        if conn is not None:
            conn.close()


def modify(data):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(" UPDATE requests SET title = %s, request = %s WHERE id = %s",
                    (
                        data['title'],
                        data['request'],
                        data['id'])
                    )

        data = cur.rowcount

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        return ("row updated", data)
    except (Exception, psycopg2.DatabaseError) as error:
        return ("Modify issue is: ", error)
    finally:
        if conn is not None:
            conn.close()
