from config.dbconfig import pg_config
import psycopg2

class ResourcesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = 'SELECT * FROM resource NATURAL JOIN water NATURAL JOIN fuel NATURAL JOIN food;'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self,r_id):
        cur = self.conn.cursor()
        q1 = "select resource_type from resource where r_id = %s;"
        cur.execute(q1,(r_id,))
        material = cur.fetchone()[0]
    
        if 'water' in material or 'fuel' in material or 'food' in material:
            query = 'SELECT * FROM resource NATURAL INNER JOIN '+ material+ ' WHERE r_id = %s;'
            cur.execute(query, (r_id,))
            result = cur.fetchone()
        else:
            query = "select* from resource where r_id = %s;"
            cur.execute(query, (r_id,))
            result = cur.fetchone()
        return result


    def getResourcesByType(self,r_type):
        cur = self.conn.cursor()
        if 'water'in r_type:
            query = 'SELECT * FROM resource NATURAL JOIN water WHERE r_type = %s;'
        elif 'fuel'in r_type:
            query = 'SELECT * FROM resource NATURAL JOIN fuel WHERE r_type = %s;'
        elif 'food'in r_type:
            query = 'SELECT * FROM resource NATURAL JOIN food WHERE r_type = %s;'
        else:
            query = 'SELECT * FROM  resource WHERE r_type = %s;'
        cur.execute(query,(r_type,))
        result = []
        for row in cur:
            result.append(row)
        return result
    
        
        
    def getResourceByLocation(self,location):
        cur = self.conn.cursor()
        #Here we decided no to be specific in full information of type like water,foods, or fuel
        query= 'SELECT * FROM resource WHERE r_location = %s;'
        cur.execute(query,(location,))
        result=[]
        for row in cur:
            result.append(row)
        return result

    def getResourcesInNeedBySenateRegion(self):
        cur = self.conn.cursor()
        query = 'SELECT requests.r_id, r_type, get_senate_region(r_location) as senate_region from resource, requests where resource.r_id = requests.r_id group by senate_region, requests.r_id, r_type order by senate_region; '
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getResourcesAvailableBySenateRegion(self):
        cur = self.conn.cursor()
        query = 'SELECT resource.r_id, r_type, get_senate_region(r_location) as senate_region from resource where r_availability = true group by senate_region, resource.r_id, r_type order by senate_region; '
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getResourcesInNeedDaily(self):
        cur = self.conn.cursor()
        query = 'select requests.r_id, r_type from resource, requests where resource.r_id = requests.r_id order by requests.r_id;'
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getResourcesAvailableDaily(self):
        cur = self.conn.cursor()
        query = 'select r_id, r_type from resource where r_availability = true order by r_id;'
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result


    """
    This can be made into a SQL function for faster functionality
    """
    def getResourcesByTypeAndLocation(self,r_type,location):
        cur = self.conn.cursor()
        if 'water'in r_type:
            query = 'SELECT * FROM resource NATURAL JOIN water WHERE r_type = %s AND r_location = %s;'
        elif 'fuel'in r_type:
            query = 'SELECT * FROM resource NATURAL JOIN fuel WHERE r_type = %s AND r_location = %s;'
        elif 'food'in r_type:
            query = 'SELECT * FROM resource NATURAL JOIN food WHERE r_type = %s AND r_location = %s;'
        else:
            query = 'SELECT * FROM  resource WHERE r_type = %s AND r_location = %s;'
        cur.execute(query,(r_type,location,))
        result = []
        for row in cur:
            result.append(row)
        return result

    
    """
    #here we don not need all info of generalized resources
    def getResourcesByAvailability(self,availability = TRUE):
        cur = self.conn.cursor()
        query = 'SELECT * FROM resource ORDER BY r_type ASC WHERE r_availability = %s;'
        cur.execute(query,(availability,))
        resutl = []
        for row in cur:
            result.append(row)
        return result
    """
    
    """
      This query function will get resources by priced 
      but it will also query the resources the are less or equal to that price
    
    def getResourceByPrice(self,price):
        cur = self.conn.cursor()
        query ="SELECT * FROM resource  ORDER BY r_type ASC WHERE r_price < = %f;"

    def getSupplierbyPartId(self,r_id):
        cur = self.conn.cursor()
        query = 'SELECT supplier_id,first_name,middle_initial, last_name,company_name, phone,email,supplier_location  FROM resource NATURAL supplier NATURAL JOIN supplies WHERE PID = %s'
        cur.execute(query(r_id,))

    """