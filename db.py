import mysql.connector
from mysql.connector import Error
import pandas as pd

#function to connect to the db
#params: host name, username, db password

# params: host name, user name and password
# returns: sql connection object if connection succesful
#           or error if unsuccessful 
# connection = none to close any previous connections

def create_connection(host, user, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user,
            passwd = password 
        )
        print("connection successful")
    except Error as err:
        print(f"Error: {err}")

    return connection 


def new_database(connection, query):
    cursor = connection.cursor()  