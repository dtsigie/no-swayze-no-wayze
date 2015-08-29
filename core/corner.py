import pymysql
import os
#Wrapper for SQL.
class Corner:
        cur = ""
        DATABASE_USER = os.environ['DATABASE_USER']
        DATABASE_HOST = os.environ['DATABASE_HOST']
        DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
        DATABASE_NAME = os.environ['DATABASE_NAME']
        
        def __init__(self):
                self.conn = pymysql.connect(user=DATABASE_USER,port=3306, passwd=DATABASE_PASSWORD, host=DATABASE_HOST, db=DATABASE_NAME)
                self.cur = self.conn.cursor()
        def query(self, query):
                self.cur.execute(query)
        def lastInsert(self):
                query = "SELECT LAST_INSERT_ID() as id;"
                result = self.query(query)
                return result