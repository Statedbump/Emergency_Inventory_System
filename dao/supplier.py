from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://djxaqudhuoodnk:4c981d57b20db4ad50339e1b5121cd03b0b5c6f2d18e67ede1877027e25e2c3c@ec2-3-223-21-106.compute-1.amazonaws.com:5432/d7d9hgkosa7fho'
        self.conn = psycopg2.connect(DATABASE_URL)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from supplier where s_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def getResourcesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        result = []
        query = "select s_id, first_name, middle_initial, last_name, r_id, r_type, water_type, measurement_unit, r_location, supply_date from resource natural inner join supplier natural inner join supplies natural inner join water where s_id =%s and r_type ='Water';"
        cursor.execute(query, (supplier_id,))
        for row in cursor:
            result.append(row)
        query = "select s_id, first_name, middle_initial, last_name, r_id, r_type, fuel_type, fuel_octane_rating, r_location, supply_date from resource natural inner join supplier natural inner join supplies natural inner join fuel where s_id =%s and r_type ='Fuel';"
        cursor.execute(query, (supplier_id,))
        for row in cursor:
            result.append(row)
        query = "select s_id, first_name, middle_initial, last_name, r_id, r_type, food_type, r_location, supply_date from resource natural inner join supplier natural inner join supplies natural join food where s_id =%s and r_type ='Food';"
        cursor.execute(query, (supplier_id,))
        for row in cursor:
            result.append(row)
        query = "select s_id, first_name, middle_initial, last_name, r_id, r_type, r_location, supply_date from resource natural inner join supplier natural inner join supplies where s_id =%s and r_type <> 'Water' and r_type <> 'Fuel' and r_type <>'Food';"
        cursor.execute(query, (supplier_id,))
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select * from supplier where supplier_location = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, first_name, middle_initial, last_name, company_name, warehouse_address, supplier_location, phone, login_id):
        cursor = self.conn.cursor()
        query = "insert into supplier(first_name, middle_initial, last_name, company_name, warehouse_address, supplier_location, phone, login_id) values (%s, %s, %s, %s, %s, %s,%s, %s) returning s_id;"
        cursor.execute(query, (first_name, middle_initial, last_name, company_name, warehouse_address, supplier_location, phone, login_id))
        s_id = cursor.fetchone()[0]
        self.conn.commit()
        return s_id

    def delete(self, s_id):
        cursor = self.conn.cursor()
        query = "delete from supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        self.conn.commit()
        return s_id

    def update(self, s_id, first_name, middle_initial, last_name, company_name, warehouse_address, supplier_location, phone, login_id):
        cursor = self.conn.cursor()
        query = "update supplier set first_name = %s, middle_initial = %s, last_name = %s, company_name = %s, warehouse_address = %s, supplier_location = %s, phone = %s, login_id = %s where s_id = %s;"
        cursor.execute(query, (first_name, middle_initial, last_name, company_name, warehouse_address, supplier_location, phone, login_id, s_id,))
        self.conn.commit()
        return s_id
