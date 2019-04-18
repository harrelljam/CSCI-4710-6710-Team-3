from flask import Flask, render_template, send_from_directory, request, session
import os
import socket
import util
import psycopg2

db_connect_command = "dbname='tempdb' user='tmp' host='localhost' password='tmp'"
app = Flask(__name__)

app_path = os.path.dirname(os.path.abspath(__file__))


def getUserName():
    userId = session.get('userid', None)
    conn = util.connect_db(db_connect_command)
    cursor = conn.cursor()
    sql_query = "select lastName from ulist where userId='" + userId + "'"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return str(result)


def checkUserExist(userName):
    conn = util.connect_db(db_connect_command)
    cursor = conn.cursor()
    sql_query = "select userId from ulist where userName='" + userName + "'"
    cursor.execute(sql_query)
    conn.commit()
    conn.close()
    return type(cursor.fetchall()) is not None


def correctCredentials(userName, Password):
    print("start check")
    conn = util.connect_db(db_connect_command)
    cursor = conn.cursor()
    print("userName " + userName)
    print("Password " + Password)
    sql_query = "select userId from ulist where userid='" + userName + "' and pwd='" + Password + "'"
    print("before execute")
    cursor.execute(sql_query)
    print(sql_query)
    rec = 0
    for row in cursor:
        rec = rec + 1
        result = row[0]
    conn.commit()
    conn.close()
    if rec > 0:
        session['userid'] = str(result)
        print("true")
        return True
    else:
        print("false")
        return False


def insertUser(userName, password, firstName, lastName):
    conn = util.connect_db(db_connect_command)
    cursor = conn.cursor()
    sql_query = "insert into ulist (userid, firstname, lastname, pwd) values('" + userName + "','" + firstName + "','" + lastName + "','" + password + "')"
    print("before execute " + sql_query)
    cursor.execute(sql_query)
    conn.commit()
    conn.close()


def connect_db(connect_command):
    conn = psycopg2.connect(connect_command)
    return conn
