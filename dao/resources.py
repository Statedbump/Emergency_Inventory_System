from config.dbconfig import pg_config
import psycopg2

class ResourcesDAO:
    def __init__(self):

        DATABASE_URL = 'postgres://djxaqudhuoodnk:4c981d57b20db4ad50339e1b5121cd03b0b5c6f2d18e67ede1877027e25e2c3c@ec2-3-223-21-106.compute-1.amazonaws.com:5432/d7d9hgkosa7fho'
        self.conn = psycopg2.connect(DATABASE_URL)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = 'SELECT * FROM resource ;'
        cursor.execute(query)
        result = []
        for row in cursor:

            result.append(row)
        return result

    def getAllResourcesRequests(self):
        cursor = self.conn.cursor()
        query = 'select p_id, requests.r_id, r_type from resource NATURAL INNER JOIN requests;'
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



        #SEARCH FUNCTIONS FOR HANDLER
 

    def getResourceById(self,r_id):
        cur = self.conn.cursor()
        q1 = "select r_type from resource where r_id = %s;"
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


    def getResourceByType(self,r_type):
        cur = self.conn.cursor()
        if 'water' in r_type or 'fuel' in r_type or 'food' in r_type:
            query = 'SELECT * FROM resource NATURAL INNER JOIN '+ r_type+ ';'
            cur.execute(query, ())
           
        else:
            query = 'SELECT * FROM  resource WHERE r_type = %s;'
            cur.execute(query,(r_type,))

        result = []
        for row in cur:
            result.append(row)
        return result

    def getResourceByLocation(self,r_location):
        cur = self.conn.cursor()
        #Here we decided no to be specific in full information of type like water,foods, or fuel
        query= 'SELECT * FROM resource WHERE r_location = %s;'
        cur.execute(query,(r_location,))
        result=[]
        for row in cur:
            result.append(row)
        return result

    def getResourcesByTypeLocationAndAvaliability(self, r_type,r_location,r_availability): 
        cur = self.conn.cursor()
        if 'water' in r_type or 'fuel' in r_type or 'food' in r_type:
            query = 'SELECT * FROM resource NATURAL INNER JOIN '+ r_type +' WHERE r_location = %s and r_availability =%s;'
            cur.execute(query,(r_location,r_availability,))
        else:
            query = 'SELECT * FROM  resource WHERE r_type = %s r_location = %s and r_availability =%s;'
            cur.execute(query,(r_type,r_location,r_availability,))

        result = []
        for row in cur:
            result.append(row)
        return result

    def getResourcesByTypeAndLocation(self,r_type,r_location):
        cur = self.conn.cursor()
        if 'water' in r_type or 'fuel' in r_type or 'food' in r_type:
            query = 'SELECT * FROM resource NATURAL INNER JOIN '+ r_type +' WHERE r_location = %s;'
            cur.execute(query,(r_location,))
        else:
            query = 'SELECT * FROM  resource WHERE r_type = %s AND r_location = %s;'
            cur.execute(query,(r_type,r_location,))
        
        result = []
        for row in cur:
            result.append(row)
        return result
    
    def getResourcesByTypeAndAvailability(self,r_type,r_availability):
        cur = self.conn.cursor()
        if 'water' in r_type or 'fuel' in r_type or 'food' in r_type:
            query = 'SELECT * FROM resource NATURAL INNER JOIN '+ r_type +' WHERE r_availability = %s;'
            cur.execute(query,(r_availability,))
        else:
            query = 'SELECT * FROM  resource WHERE r_type = %s AND r_availability = %s;'
            cur.execute(query,(r_type,r_availability,))
        
        result = []
        for row in cur:
            result.append(row)
        return result
    
    def getResourcesByLocationAndAvailability(self,r_location,r_availability):
        cur = self.conn.cursor()
        
        query = 'SELECT * FROM  resource WHERE r_location = %s AND r_availability = %s;'
        cur.execute(query,(r_location,r_availability,))
        
        result = []
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

    def getSupplierByResourceId(self,r_id):
        curr = self.conn.cursor()
        query = "select * from supplier NATURAL INNER JOIN supplies where r_id = %s"
        curr.execute(query, (r_id,))
        result = []
        for row in curr:
            result.append(row)
        return result

    def getPersonByResourceId(self,r_id):# This should be get person by requested r-id or by purchased r_id or reserved r_id
        curr = self.conn.cursor()
        query = "select * from supplier NATURAL INNER JOIN supplies where r_id = %s"
        curr.execute(query, (r_id,))
        result = []
        for row in curr:
            result.append(row)
        return result


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

    #Insert Update Delete
     def insert(self,r_type ,r_quantity, r_location ,r_price,r_availability,  
                , water_type= None ,measurement_unit = None 
                ,fuel_type= None , fuel_octane_rating = None
                ,food_type = None 
                ,g_brand=None , g_fuel_type =None ,g_power = None
                , batt_type = None, batt_volts = None )
        
        cursor = self.conn.cursor()
        q = "insert into resource(r_type ,r_quantity, r_location ,r_price,r_availability) values(%s,%s,%s,%s,%s) RETURNING r_id;"
        cursor.execute(q,(r_type,r_quantity,r_location,r_price,r_availability,))
        r_id = cursor.fetchone()[0]

        if 'water' in str.lower(r_type) and water_type is not None and measurement_unit is not NONE:
            q2 = "insert into water(water_type, measurement_unit,r_id) values(%s,%s,%s);"
            cursor.execute(q2,(water_type,measurement_unit,r_id,))
        elif 'food' in str.lower(r_type) and food_type is not None:
            q2 = "insert into food(food_type,r_id) values(%s,%s);"
            cursor.execute(q2,(food_type,r_id))
        elif 'fuel'in str.lower(r_type) and fuel_type is not None and fuel_octane_rating is not None:
            q2 = "inser into fuel(fuel_type, fuel_octane_rating, r_id) values(%s,%s,%s);"
            cursor.execute(q2,(fuel_type,fuel_octane_rating,r_id))
        elif 'generator' in str.lower(r_type) and g_brand is not None and g_fuel_type is not None and g_power is not None:
            q2 = 'insert into generator(g_brand,g_fuel_type,g_power,r_id) values(%s,%s,%s,%s);'
            cursor.execute(q2,(g_brand,g_fuel_type,g_power,r_id,))
        elif 'battery' in str.lower(r_type) and batt_type is not None and batt_volts is not None:
            q2 = "insert into battery(batt_type,batt_volts,r_id) values(%s,%s,%s);"
            cursor.execute(q2,(batt_type,batt_volts,r_id))
        self.conn.commit()
        return r_id

            




    def delete(self, r_id):
         cur = self.conn.cursor()
         q = "DELETE FROM resource WHERE r_id = %s"
         cur.execute(q,(r_id,))
         self.conn.commit()
         return r_id

    def update(self,r_id ,r_type ,r_quantity, r_location ,r_price,r_availability,  
                , water_type= None ,measurement_unit = None 
                ,fuel_type= None , fuel_octane_rating = None
                ,food_type = None 
                ,g_brand=None , g_fuel_type =None ,g_power = None
                , batt_type = None, batt_volts = None )
        
        cursor = self.conn.cursor()
        q1 = 'UPDATE resource set r_type=%s, r_quantity = %s,r_price =%s,r_avaliability = %s where r_id = %s;'
        cursor.execute(q1,(r_type,r_quantity,r_location,r_price,r_availability,r_id,))

        if 'water' in str.lower(r_type):
            if water_type is not None and  measurement_unit  is not None:
                q2 = "UPDATE water set water_type = %s , measurement_unit = %s where r_id = %s;"
                cursor.execute(q2,(w_type,measurement_unit,r_id,))
            elif water_type is None and measurement_unit is not None:
                q2 = "UPDATE water set measurement_unit = %s where r_id = %s;"
                cursor.execute(q2,(measurement_unit,r_id,))
            elif water_type is not None and measurement_unit is None:
                q2 = "UPDATE water set water_type = %s  where r_id = %s;"
                cursor.execute(q2,(w_type,r_id,))

        elif 'fuel' in str.lower(r_type):
            if fuel_type is not None and  fuel_octane_rating is not None:
                q2 = "UPDATE fuel set fuel_type = %s , fuel_octane_rating = %s where r_id = %s;"
                cursor.execute(q2,(fuel,fuel_octane_rating,r_id,))
            elif fuel_type is None and measurement_unit  is not None:
                q2 = "UPDATE fuel set measurement_unit = %s where r_id = %s;"
                cursor.execute(q2,(measurement_unit,r_id,))
            elif fuel_type is not None and measurement_unit is None:
                q2 = "UPDATE fuel set fuel_type = %s  where r_id = %s;"
                cursor.execute(q2,(fuel_type,r_id,))

         elif 'food' in str.lower(r_type):
            if fuel_type is not None: 
                q2 = "UPDATE food set food_type = %s  where r_id = %s;"
                cursor.execute(q2,(food_type,r_id,))

        elif 'generator' in str.lower(r_type):
            if g_brand is not None and  g_fuel_type is not None and g_power is not None :
                q2 = "UPDATE generator set g_brand = %s, g_fuel_type = %s, g_power = %s where r_id = %s;"
                cursor.execute(q2,(g_brand,g_fuel_type,g_power,r_id,))
            elif g_brand is None and  g_fuel_type is not None and g_power is not None :
                q2 = "UPDATE generator set g_fuel_type = %s, g_power = %s where r_id = %s;"
                cursor.execute(q2,(g_fuel_type,g_power,r_id,))
            elif g_brand is not None and  g_fuel_type is None and g_power is not None :
                q2 = "UPDATE generator set g_brand = %s, g_power = %s where r_id = %s;"
                cursor.execute(q2,(g_brand,g_power,r_id,))
            elif g_brand is not None and  g_fuel_type is not None and g_power is  None :
                q2 = "UPDATE generator set g_brand = %s, g_fuel_type = %s where r_id = %s;"
                cursor.execute(q2,(g_brand,g_fuel_type,r_id,))
            elif g_brand is not None and  g_fuel_type is None and g_power is  None :
                q2 = "UPDATE generator set g_brand = %s where r_id = %s;"
                cursor.execute(q2,(g_brand,r_id,))
            elif g_brand is None and  g_fuel_type is not None and g_power is  None :
                q2 = "UPDATE generator set g_fuel_type = %s where r_id = %s;"
                cursor.execute(q2,(g_fuel_type,r_id,))
            elif g_brand is None and  g_fuel_type is None and g_power is not None :
                q2 = "UPDATE generator set g_power = %s where r_id = %s;"
                cursor.execute(q2,(g_power,r_id,))

        elif 'battery' in str.lower(r_type):
            if batt_type is not None and  batt_volts  is not None:
                q2 = "UPDATE battery set batt_type = %s , batt_volts = %s where r_id = %s;"
                cursor.execute(q2,(w_type,batt_volts,r_id,))
            elif batt_type is None and batt_volts is not None:
                q2 = "UPDATE battery set batt_volts = %s where r_id = %s;"
                cursor.execute(q2,(batt_volts,r_id,))
            elif batt_type is not None and batt_volts is None:
                q2 = "UPDATE battery set batt_type = %s  where r_id = %s;"
                cursor.execute(q2,(batt_type,r_id,))
        self.conn.commit()

        return r_id
            
        

