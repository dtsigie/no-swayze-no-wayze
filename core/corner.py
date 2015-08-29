import pymysql
import envVariables

#Wrapper for SQL.
class Corner:
        cur = ""
                
        def __init__(self):
                self.conn = pymysql.connect(user=DATABASE_USER,port=3306, passwd=DATABASE_PASSWORD, host=DATABASE_HOST, db=DATABASE_NAME)
                self.cur = self.conn.cursor()
        def query(self, query):
                self.cur.execute(query)
        def lastInsert(self):
                query = "SELECT LAST_INSERT_ID() as id;"
                result = self.query(query)
                return result