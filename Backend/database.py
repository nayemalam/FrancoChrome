import sqlite3
import os


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
        print("Could not connect to database")
 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """ 
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)
        print("Could not create database")

if __name__ == '__main__':
    conn = create_connection(os.getcwd() + "/database/database.db")
    create_table(conn,
    '''
    CREATE TABLE words (
    wid int(11) NOT NULL UNIQUE,
    word varchar(500) NOT NULL,
    translation varchar(500),
    PRIMARY KEY (wid)
    );
    ''')
    create_table(conn,
    '''
    CREATE TABLE users (
    uid TEXT NOT NULL UNIQUE,
    last_refresh TEXT NOT NULL,
    PRIMARY KEY (uid)
    );
    ''')
    create_table(conn,
    '''
    CREATE TABLE seen (
    uid TEXT,
    wid int(11),
    FOREIGN KEY (uid) REFERENCES users(uid),
    FOREIGN KEY (wid) REFERENCES words(wid),
    PRIMARY KEY (uid, wid)
    );
    ''')
    conn.close()