from config.dbconfig import pg_config
import psycopg2

class PersonDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPerson(self):
        cursor = self.conn.cursor()
        query = "select * from person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPersonById(self, p_id):
        cursor = self.conn.cursor()
        query = "select * from person where p_id = %s;"
        cursor.execute(query, (p_id,))
        result = cursor.fetchone()
        return result

    def getReservedResourcesByPersonId(self, p_id):
        cursor = self.conn.cursor()
        #Reserved resources
        result = []
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, water_type, measurement_unit, resource_total, reserve_date from resource natural inner join person natural inner join reserves natural inner join water where p_id =%s and r_type ='Water';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, fuel_type, fuel_octane_rating, resource_total, reserve_date from resource natural inner join person natural inner join reserves natural inner join fuel where p_id =%s and r_type ='Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, food_type, resource_total, reserve_date from resource natural inner join person natural inner join reserves natural inner join food where p_id =%s and r_type ='Food';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, resource_total, reserve_date from person natural inner join reserves natural inner join resource where p_id = %s and r_type <> 'Food' and r_type <> 'Water' and r_type <> 'Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        return result

    def getPurchasedResourcesByPersonId(self, p_id):
        #Bought resources
        cursor = self.conn.cursor()
        result = []
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, water_type, measurement_unit, resource_total, o_date from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join water where p_id =%s and r_type ='Water';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, fuel_type, fuel_octane_rating, resource_total, o_date from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join fuel where p_id =%s and r_type ='Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, food_type, resource_total, o_date from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join food where p_id =%s and r_type ='Food';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, resource_total, o_date from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys where p_id =%s and r_type <> 'Food' and r_type <> 'Water' and r_type <> 'Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        return result

    def getPersonByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select * from person where location_of_p = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def requestResource(self, p_id, r_id, request_quantity):
        cursor = self.conn.cursor()
        query = "insert into requests(p_id, r_id, request_quantity) values (%s, %s, %s);"
        cursor.execute(query, (p_id,r_id,request_quantity,))
        self.conn.commit()
        return p_id

    def insert(self, first_name, middle_initial, last_name, email, location_of_p, phone, login_id):
        cursor = self.conn.cursor()
        query = "insert into person(first_name, middle_initial, last_name, email, location_of_p, phone, login_id) values (%s, %s, %s, %s, %s, %s, %s) returning p_id;"
        cursor.execute(query, (first_name, middle_initial, last_name, email, location_of_p, phone, login_id,))
        p_id = cursor.fetchone()[0]
        self.conn.commit()
        return p_id

    def delete(self, p_id):
        cursor = self.conn.cursor()
        query = "delete from person where p_id = %s;"
        cursor.execute(query, (p_id,))
        self.conn.commit()
        return p_id

    def update(self, p_id, first_name, middle_initial, last_name, email, location_of_p, phone, login_id):
        cursor = self.conn.cursor()
        query = "update person set first_name = %s, middle_initial = %s, last_name = %s, email = %s, location_of_p = %s, phone = %s, login_id = %s where p_id = %s;"
        cursor.execute(query, (first_name, middle_initial, last_name, email, location_of_p, phone, login_id, p_id,))
        self.conn.commit()
        return p_id

    def getRequestedResourcesByPersonId(self, p_id):
        cursor = self.conn.cursor()
        # Requested resources
        result = []
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type,r_location, r_quantity, water_type, measurement_unit, r_availability   from resource natural inner join person natural inner join requests natural inner join water where p_id =%s and r_type ='Water';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, r_location, r_quantity, fuel_type, fuel_octane_rating,r_availability from resource natural inner join person natural inner join requests natural inner join fuel where p_id =%s and r_type ='Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, r_location, r_quantity, food_type,r_availability from resource natural inner join person natural inner join requests natural inner join food where p_id =%s and r_type ='Food';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select p_id, first_name, middle_initial, last_name, r_id, r_type, r_location, r_quantity,r_availability from resource natural inner join person natural inner join requests where p_id =%s and r_type <> 'Food' and r_type <> 'Water' and r_type <> 'Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        return result
