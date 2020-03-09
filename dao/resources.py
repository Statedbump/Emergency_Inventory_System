from config.dbconfig import pg_config
import psycopg2

class ResourcesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host']
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)   
    """"Fix to make so resources that are generalized like fuel and water get joind and showned get joinced too """"
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
        q1 = "select resource_type from resource where r_id = %s"
        cur.execute(q1,(r_id,))
        material = cur1.fetchone()[0]
    
        if material is 'water'or 'fuel' or 'food':
            query = 'SELECT * FROM resource NATURAL JOIN '+ material+ ' WHERE r_id = %s'
            cur.execute(query, (r_id,))
            result = cur.fetchone()
        else:
            query = "select* from resource where r_id = %s"
            cur.execute(query, (r_id,))
            result = cur.fetchone()
        return result
    def getResourceByType():
    def getResourceByLocation():
    
