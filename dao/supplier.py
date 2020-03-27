from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSupplier(self):
        cursor = self.conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = cursor.fetchone()
        return result

    def getResourcesBySupplierId(self, s_id):
        cursor = self.conn.cursor()
        #Requested resources
        result = []
        query = "select r_id, r_type, water_type, measurement_unit, r_location, resource_total, request_date from resource natural inner join supplier natural inner join requests natural inner join water where s_id =%s and r_type ='Water';"
        cursor.execute(query, (s_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, fuel_type, fuel_octane_rating, r_location, resource_total, request_date from resource natural inner join supplier natural inner join requests natural inner join fuel where s_id =%s and r_type ='Fuel';"
        cursor.execute(query, (s_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, food_type, r_location, resource_total, request_date from resource natural inner join supplier natural inner join requests natural inner join food where s_id =%s and r_type ='Food';"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, resource_total, request_date from resource natural inner join supplier natural inner join requests where s_id =1 and r_type <> 'Food' and r_type <> 'Water' and r_type <> 'Fuel';"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)

        #Bought resources
        query = "select r_id, r_type, water_type, measurement_unit, r_location, resource_total, o_date from resource natural inner join supplier natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join water where s_id =%s and r_type ='Water';"
        cursor.execute(query, (s_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, fuel_type, fuel_octane_rating, r_location, resource_total, o_date from resource natural inner join supplier natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join fuel where s_id =%s and r_type ='Fuel';"
        cursor.execute(query, (s_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, food_type, r_location, resource_total, o_date from resource natural inner join supplier natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join food where s_id =%s and r_type ='Food';"
        cursor.execute(query, (s_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, resource_total, o_date from resource natural inner join supplier natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys where s_id =%s and r_type <> 'Food' and r_type <> 'Water' and r_type <> 'Fuel';"
        cursor.execute(query, (s_id,))
        for row in cursor:
            result.append(row)
        return result

    def insert(self, first_name, middle_initial, last_name, location_of_s, company_name, warehouse_address, phone, login_id):
        cursor = self.conn.cursor()
        query = "insert into supplier(first_name, middle_initial, last_name, location_of_s, company_name, warehouse_address, phone, login_id) values (%s, %s, %s, %s, %s, %s, %s, %s) returning s_id;"
        cursor.execute(query, (first_name, middle_initial, last_name, location_of_s, company_name, warehouse_address, phone, login_id))
        s_id = cursor.fetchone()[0]
        self.conn.commit()
        return s_id

    def delete(self, s_id):
        cursor = self.conn.cursor()
        query = "delete from supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        self.conn.commit()
        return s_id

    def update(self, s_id, first_name, middle_initial, last_name, location_of_s, company_name, warehouse_address, phone, login_id):
        cursor = self.conn.cursor()
        query = "update supplier set first_name = %s, middle_initial = %s, last_name = %s,location_of_s = %s, company_name = %s, warehouse_address = %s, phone = %s, login_id = %s where s_id = %s;"
        cursor.execute(query, (first_name, middle_initial, last_name, location_of_s, company_name, warehouse_address, phone, login_id, s_id,))
        self.conn.commit()
        return s_id
