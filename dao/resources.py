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

    def getAllResourcesRequests(self):
        cursor = self.conn.cursor()
        query = 'select p_id, requests.r_id, r_type from resource, requests where resource.r_id = requests.r_id order by p_id,requests.r_id;'
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllResourcesAvailable(self):
        cursor = self.conn.cursor()
        query = 'select r_id, r_type, r_availability from resource where r_availability= true;'
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def sortResourcesRequestsByResourceName(self):
        cursor = self.conn.cursor()
        query = 'select p_id, requests.r_id, r_type from resource, requests where resource.r_id = requests.r_id order by r_type;'
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def sortResourcesAvailableByResourceName(self):
        cursor = self.conn.cursor()
        query = 'select r_id, r_type, r_availability from resource where r_availability= true order by r_type;'
        cursor.execute(query, )
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
        query = 'SELECT requests.p_id, requests.r_id, r_type, request_quantity, get_senate_region(r_location) as senate_region from resource natural inner join requests group by senate_region, requests.p_id, requests.r_id, request_quantity, r_type order by senate_region;'
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getResourcesAvailableBySenateRegion(self):
        cur = self.conn.cursor()
        query = 'SELECT r_id, r_type, r_quantity, get_senate_region(r_location) as senate_region from resource where r_availability = true group by senate_region, r_id, r_type, r_quantity order by senate_region;'
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getResourcesInNeedDaily(self):
        cur = self.conn.cursor()
        query = 'select p_id, requests.r_id, r_type, request_quantity, request_date from resource natural inner join requests where request_date = current_date order by p_id, requests.r_id;'
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getResourcesAvailableDaily(self):
        cur = self.conn.cursor()
        query = 'select r_id, r_type, r_quantity , current_date from resource where r_availability = true order by r_id;'
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getResourcesInNeedWeekly(self):
        cur = self.conn.cursor()
        query = "select p_id, requests.r_id, r_type, request_quantity, request_date from resource natural inner join requests where request_date >= now() - interval "+"'"+"7 days"+"'"+" order by p_id, requests.r_id;"
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getResourcesAvailableWeekly(self):
        cur = self.conn.cursor()
        query = "select r_id, r_type, r_quantity , supplies.supply_date from resource natural inner join supplies where r_availability = true and supplies.supply_date >= now() - interval "+"'"+"7 days"+"'"+" order by r_id;"
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getLocationByResourceId(self, r_id):
        cur = self.conn.cursor()
        query = "select r_location from resource where r_id = %s;"
        cur.execute(query, (r_id,))
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

    def getCountResourcesInNeedBySenateRegion(self):
        cur = self.conn.cursor()
        query = 'select sr.r_type, sum(sr.request_quantity) as resources_in_need, sr.senate_region from (SELECT requests.p_id, requests.r_id, r_type, request_quantity, get_senate_region(r_location) as senate_region from resource natural inner join requests group by senate_region, requests.p_id, requests.r_id, request_quantity, r_type order by senate_region) as sr group by sr.r_type, sr.senate_region order by sr.r_type, sr.senate_region;'
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getCountResourcesAvailableBySenateRegion(self):
        cur = self.conn.cursor()
        query = 'select sr.r_type, sum(sr.r_quantity) as resources_available, sr.senate_region from (SELECT r_id, r_type, r_quantity, get_senate_region(r_location) as senate_region from resource where r_availability = true group by senate_region, r_id, r_type, r_quantity order by senate_region) as sr group by sr.r_type, sr.senate_region order by sr.r_type, sr.senate_region;'
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getCountResourcesInNeedDaily(self):
        cur = self.conn.cursor()
        query = 'select d.r_type, sum(d.request_quantity) as resources_in_need, d.request_date from (select p_id, requests.r_id, r_type, request_quantity, request_date from resource natural inner join requests where request_date = current_date order by p_id, requests.r_id) as d group  by d.r_type, d.request_date order by d.r_type;'
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getCountResourcesAvailableDaily(self):
        cur = self.conn.cursor()
        query = 'select d.r_type, sum(d.r_quantity) as resources_available, d.current_date from (select r_id, r_type, r_quantity , current_date from resource where r_availability = true order by r_id) as d group by d.r_type, d.current_date order by d.r_type;'
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getCountResourcesInNeedWeekly(self):
        cur = self.conn.cursor()
        query = "select d.r_type, sum(d.request_quantity) as resources_in_need, d.request_date from (select p_id, requests.r_id, r_type, request_quantity, request_date from resource natural inner join requests where request_date >= now() - interval "+"'"+"7 days"+"'"+" order by p_id, requests.r_id) as d group  by d.r_type, d.request_date order by d.r_type;"
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result

    def getCountResourcesAvailableWeekly(self):
        cur = self.conn.cursor()
        query = "select d.r_type, sum(d.r_quantity) as resources_available, d.supply_date from (select r_id, r_type, r_quantity , supply_date from resource natural inner join supplies where r_availability = true and supply_date >= now() - interval "+"'"+"7 days"+"'"+" order by r_id) as d group by d.r_type, d.supply_date order by d.r_type;"
        cur.execute(query, )
        result = []
        for row in cur:
            result.append(row)
        return result



