import mysql.connector
from mysql.connector import Error
import pandas as pd

# Queries
# either use f strings or a function to return a query.
# TODO Add queries as strings to be called
CREATE_PASS_TABLE = """
CREATE TABLE securePassword ()
"""

HEADING_PASS_TABLE = """
INSERT INTO securePassword ('Service', 'Key', 'Tag', 'Encrypted Pass', 'nonce');
"""

# Query for adding a new password,
# Reqd: service, key, tag, encrypted pass, nonce

ADD_PASSWORD = """
INSERT INTO securePassword VALUES()
"""


# function to connect to the db
# params: host name, username, db password

# params: host name, user name and password (database name)
# returns: sql connection object if connection succesful
#           or error if unsuccessful
# connection = none to close any previous connections

# for first time connection, check if db exists, else
def create_connection(host, user, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password
            # database = db_name
            # argument if database already exists
        )
        print("connection successful")
    except Error as err:
        print(f"Error: {err}")

    return connection


def new_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("database created")
    except Error as er:
        print(f"Error: {er}")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("query successful")
    except Error as er:
        print(f"error: {er}")




def add_password_query(service, key, tag, password, nonce):
    """
    params: takes service, key, tag, encrypted pass, nonce
    returns: sql query to insert new password.
    """
    # key_string = key.decode()
    # tag_string = tag.decode()
    # pass_string = password.decode()
    # nonce_string = nonce.decode()
    return f"""INSERT INTO securePassword VALUES("{service}", "{key}", "{tag}", "{password}", "{nonce}")"""


def get_password_query():
    pass