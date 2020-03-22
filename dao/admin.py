from config.dbconfig import pg_config
import psycopg2

class AdminDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAdmin(self):
        cursor = self.conn.cursor()
        query = "select * from admin;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminById(self, adm_id):
        cursor = self.conn.cursor()
        query = "select * from admin where adm_id = %s;"
        cursor.execute(query, (adm_id,))
        result = cursor.fetchone()
        return result

    #def getResourcesByAdminId(self, adm_id):
     #   cursor = self.conn.cursor()
      #  result = []
      #  query = "select r_id, r_type, water_type, measurement_unit, r_location, resource_total,"

    def insert(self, permission_key, p_id):
        cursor = self.conn.cursor()
        query = "insert into admin(permission_key, p_id) values (%s, %s) returning adm_id;"
        cursor.execute(query, (permission_key, p_id,))
        adm_id = cursor.fetchone()[0]
        self.conn.commit()
        return adm_id

    def delete(self, adm_id):
        cursor = self.conn.cursor()
        query = "delete from admin where adm_id = %s;"
        cursor.execute(query, (adm_id,))
        self.conn.commit()
        return adm_id

    def update(self, adm_id, permission_key, p_id):
        cursor = self.conn.cursor()
        query = "update admin set permission_key = %s, p_id = %s where adm_id = %s;"
        cursor.execute(query, (permission_key,p_id, adm_id,))
        self.conn.commit()
        return adm_id




