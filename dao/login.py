from config.dbconfig import pg_config
import psycopg2

class LoginDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://djxaqudhuoodnk:4c981d57b20db4ad50339e1b5121cd03b0b5c6f2d18e67ede1877027e25e2c3c@ec2-3-223-21-106.compute-1.amazonaws.com:5432/d7d9hgkosa7fho'
        self.conn = psycopg2.connect(DATABASE_URL)

    def getAllLogin(self):
        cursor = self.conn.cursor()
        query = "select * from login;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLoginById(self, login_id):
        cursor = self.conn.cursor()
        query = "select * from login where login_id = %s;"
        cursor.execute(query, (login_id,))
        result = cursor.fetchone()
        return result

    def insertLogin(self, username, password):
        cursor = self.conn.cursor()
        query = "insert into login(username, password) values (%s, %s) returning login_id;"
        cursor.execute(query, (username, password))
        login_id = cursor.fetchone()[0]
        self.conn.commit()
        return login_id

    def deleteLogin(self, login_id):
        cursor = self.conn.cursor()
        query = "delete from login where login_id = %s;"
        cursor.execute(query, (login_id,))
        self.conn.commit()
        return login_id

    def updateLogin(self, login_id, username, password):
        cursor = self.conn.cursor()
        query = "update login set username = %s, password = %s where login_id = %s;"
        cursor.execute(query, (username, password, login_id,))
        self.conn.commit()
        return login_id




