from config.dbconfig import pg_config
import psycopg2

class PersonDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
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
        query = "select r_id, r_type, water_type, measurement_unit, r_location, resource_total, request_date from resource natural inner join person natural inner join requests natural inner join water where p_id =%s and r_type ='Water';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, fuel_type, fuel_octane_rating, r_location, resource_total, request_date from resource natural inner join person natural inner join requests natural inner join fuel where p_id =%s and r_type ='Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, food_type, r_location, resource_total, request_date from resource natural inner join person natural inner join requests natural inner join food where p_id =%s and r_type ='Food';"
        cursor.execute(query, (p_id,))
        result = []
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, resource_total, request_date from resource natural inner join person natural inner join requests where p_id =1 and r_type <> 'Food' and r_type <> 'Water' and r_type <> 'Fuel';"
        cursor.execute(query, (p_id,))
        result = []
        for row in cursor:
            result.append(row)

        #Bought resources
        query = "select r_id, r_type, water_type, measurement_unit, r_location, resource_total, o_date from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join water where p_id =%s and r_type ='Water';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, fuel_type, fuel_octane_rating, r_location, resource_total, o_date from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join fuel where p_id =%s and r_type ='Fuel';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, food_type, r_location, resource_total, o_date from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys natural inner join food where p_id =%s and r_type ='Food';"
        cursor.execute(query, (p_id,))
        for row in cursor:
            result.append(row)
        query = "select r_id, r_type, r_location, resource_total, o_date from resource natural inner join person natural inner join offers natural inner join payment natural inner join resource_order natural inner join buys where p_id =%s and r_type <> 'Food' and r_type <> 'Water' and r_type <> 'Fuel';"
        cursor.execute(query, (p_id,))
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
