import mysql.connector # pip install mysql-connector-python

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistema_tickets"
    )
