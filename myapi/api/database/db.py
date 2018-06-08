import json
import psycopg2
from myapi.api.database.config import config
from psycopg2.extras import RealDictCursor

def view_users():

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=RealDictCursor)

        view_users= """ SELECT * FROM users """
        cur.execute(view_users)
        
        #
        print (json.dumps(cur.fetchall(), indent=2))
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error view users")
    finally:
        if conn is not None:
            conn.close()

def add_user(data):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("INSERT INTO USERS (firstname,lastname,username, role, password) values(%s,%s,%s,%s,%s)",
        (
        data['firstname'],
        data['lastname'],
        data['username'],
        data['role'],
        data['password']    )
        )
        
        
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def login(username, password):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=RealDictCursor)

        view_users= """ SELECT * FROM users """
        cur.execute(view_users)
        
        #
        users = cur.fetchall()
        # search through the db
        # return True
#   Tafuta njia ya kufanya hii function iwork ama tafuta ingine
        msee = [i for i in users if i['username'] == username and i['password'] == password]
        if msee == None:
            return False
        else: 
            return True
        # for i in users:
        #     if i['username'] == username and i['password'] == password:
        #         return True
        #     else:
        #         print(username)
        #         return False
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
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

        cur.execute("INSERT INTO requests (title, request) values(%s,%s)",
        (
        data['title'],
        data['request']
          )
        )
        
        
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def view_user_requests(username):
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=RealDictCursor)

        view_requests = """ SELECT * FROM requests """
        cur.execute(view_requests)
        
        #convert to list of dictionaries
        requests = json.dumps(cur.fetchall(), indent=2)
        # view requests
        request = [request for request in requests if request["username"] == username]
        return request
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_request_id(username, id):
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=RealDictCursor)

        view_requests = """ SELECT * FROM requests """
        cur.execute(view_requests)
        
        #convert to list of dictionaries
        requests = json.dumps(cur.fetchall(), indent=2)
        # view requests
        dicts = view_user_requests(username)
        result = next(
            (item for item in dicts if item["id"] == id), False)
        return result
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def edit_request(username, id, title, request):
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=RealDictCursor)

        view_requests = """ SELECT * FROM requests """
        cur.execute(view_requests)
        
        #convert to list of dictionaries
        requests = json.dumps(cur.fetchall(), indent=2)
        # view requests
        result = get_request_id(username, id)
        result['title'] = title
        result['request'] = request
        #edit to db
        cur.execute("UPDATE requests (title, request) values(%s,%s)",
        (
        data['title'],
        data['request']
          )
        )
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()