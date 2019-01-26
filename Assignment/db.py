import pymysql
from pymysql.connections import Connection


def conn():
    connection: Connection = pymysql.connect(host='localhost', user='root', password='', db='bookstore', )
    return connection
