import psycopg2
from config import config


class connect ():

    def __init__(self):
        self.conn = None

    def read(self):
        try:
            # read connection parameters
            params = config()
    
            # connect to the PostgreSQL server
            print ('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)
            print(self.conn)
        except:
            print("Connecting to the Database Failed")
    
    def execute(statement):
        try:
            # create a cursor
            cur = self.conn.cursor()

            # execute a statement
            print ('Executing statement')
            cur.execute(str(statement))
            return "Statement executed"
        
        except:
            return ("Statement did not execute")
    
    def close(self):
        # create a cursor
        cur = self.conn.cursor()
        # close connection
        cur.close()


