import psycopg2
from config import config
 
 
def create_tables():
    """ 
    create tables in the database
    """
    table_structure = (
        """
        CREATE TABLE IF NOT EXISTS users (
            firstname VARCHAR(50) NOT NULL,
            lastname VARCHAR(50) NOT NULL,
            username VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY,
            role VARCHAR(10) NOT NULL,
            password VARCHAR(100) NOT NULL
        
        )
        """,
        """ 
        CREATE TABLE IF NOT EXISTS requests (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            request VARCHAR(100) NOT NULL
            
            )
        """
        
    )

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for table in table_structure:
            cur.execute(table)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()