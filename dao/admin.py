from config.dbconfig import pg_config
import psycopg2

class AdminDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://djxaqudhuoodnk:4c981d57b20db4ad50339e1b5121cd03b0b5c6f2d18e67ede1877027e25e2c3c@ec2-3-223-21-106.compute-1.amazonaws.com:5432/d7d9hgkosa7fho'
        self.conn = psycopg2.connect(DATABASE_URL)

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

    def manageResource(self, admin_id, r_id):
        cursor = self.conn.cursor()
        query = "insert into manages(admin_id, r_id) values (%s, %s);"
        cursor.execute(query, (admin_id, r_id,))
        self.conn.commit()
        return admin_id

    def getResourcesByAdminId(self, admin_id):
        cursor = self.conn.cursor()
        result = []
        query = "select r_id, r_type, r_quantity, r_location, water_type, measurement_unit, r_availability, admin_id from resource natural inner join administrator natural inner join manages natural inner join water where admin_id =%s and r_type ='Water';"
        cursor.execute(query, (admin_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_quantity, r_location,fuel_type, fuel_octane_rating,r_availability, admin_id from resource natural inner join administrator natural inner join manages natural inner join fuel where admin_id =%s and r_type ='Fuel';"
        cursor.execute(query, (admin_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_quantity, r_location, food_type, r_availability, admin_id from resource natural inner join administrator natural inner join manages natural join food where admin_id =%s and r_type ='Food';"
        cursor.execute(query, (admin_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_quantity, r_location, r_availability, admin_id from resource natural inner join administrator natural inner join manages where admin_id =%s and r_type <> 'Water' and r_type <> 'Fuel' and r_type <>'Food';"
        cursor.execute(query, (admin_id,))
        for row in cursor:
            result.append(row)
        return result




