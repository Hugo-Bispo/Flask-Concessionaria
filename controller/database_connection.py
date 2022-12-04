import mysql.connector


def mysql_connector():
    mybd = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd = "12345678",
        database="CONCESSIONARIA",
    )
    return mybd

def mysql_execute_command(command):
    mydb = mysql_connector()
    cursor = mydb.cursor()
    cursor.execute(command)
    mydb.commit()
    mydb.close()

def mysql_execute_select(query):
    mydb = mysql_connector()
    cursor = mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def mysql_execute_select_all(query):
    mydb = mysql_connector()
    cursor = mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result