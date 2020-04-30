from config.dbconfig import pg_config
import psycopg2

class LoginDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

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




