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

    def getResourcesByPersonId(self, p_id):
        cursor = self.conn.cursor()
        #Requested resources
        result = []
        query = "select r_id, r_type,r_location, resource_total, water_type, measurement_unit  from resource natural inner join person natural inner join reserves natural inner join water where p_id =%s and r_type ='Water';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, resource_total, fuel_type, fuel_octane_rating from resource natural inner join person natural inner join reserves natural inner join fuel where p_id =%s and r_type ='Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, resource_total, food_type from resource natural inner join person natural inner join reserves natural inner join food where p_id =%s and r_type ='Food';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, resource_total from resource natural inner join person natural inner join reserves where p_id =1 and r_type <> 'Food' and r_type <> 'Water' and r_type <> 'Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)

        #Bought resources
        query = "select r_id, r_type, r_location, resource_total, water_type, measurement_unit from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join water where p_id =%s and r_type ='Water';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, resource_total, fuel_type, fuel_octane_rating from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join fuel where p_id =%s and r_type ='Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, resource_total, food_type from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join food where p_id =%s and r_type ='Food';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, resource_total from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys where p_id =%s and r_type <> 'Food' and r_type <> 'Water' and r_type <> 'Fuel';"
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
        query = "select r_id, r_type,r_location, r_quantity, water_type, measurement_unit, r_availability   from resource natural inner join person natural inner join requests natural inner join water where p_id =%s and r_type ='Water';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, r_quantity, fuel_type, fuel_octane_rating,r_availability from resource natural inner join person natural inner join requests natural inner join fuel where p_id =%s and r_type ='Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, r_quantity, food_type,r_availability from resource natural inner join person natural inner join requests natural inner join food where p_id =%s and r_type ='Food';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, r_quantity,r_availability from resource natural inner join person natural inner join requests where p_id =1 and r_type <> 'Food' and r_type <> 'Water' and r_type <> 'Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        return result
