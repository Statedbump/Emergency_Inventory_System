from config.dbconfig import pg_config
import psycopg2

class AdminDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAdmin(self):
        cursor = self.conn.cursor()
        query = "select * from administrator;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminById(self, admin_id):
        cursor = self.conn.cursor()
        query = "select * from administrator where admin_id = %s;"
        cursor.execute(query, (admin_id,))
        result = cursor.fetchone()
        return result

    def insertAdmin(self, permission_key, p_id):
        cursor = self.conn.cursor()
        query = "insert into administrator(permission_key, p_id) values (%s, %s) returning admin_id;"
        cursor.execute(query, (permission_key, p_id,))
        admin_id = cursor.fetchone()[0]
        self.conn.commit()
        return admin_id

    def deleteAdmin(self, admin_id):
        cursor = self.conn.cursor()
        query = "delete from administrator where admin_id = %s;"
        cursor.execute(query, (admin_id,))
        self.conn.commit()
        return admin_id

    def updateAdmin(self, admin_id, permission_key, p_id):
        cursor = self.conn.cursor()
        query = "update administrator set permission_key = %s, p_id = %s where admin_id = %s;"
        cursor.execute(query, (permission_key,p_id, admin_id,))
        self.conn.commit()
        return admin_id




