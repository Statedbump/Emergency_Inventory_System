from flask import jsonify

from config.dbconfig import pg_config
import psycopg2

class PersonDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://djxaqudhuoodnk:4c981d57b20db4ad50339e1b5121cd03b0b5c6f2d18e67ede1877027e25e2c3c@ec2-3-223-21-106.compute-1.amazonaws.com:5432/d7d9hgkosa7fho'
        self.conn = psycopg2.connect(DATABASE_URL)

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

    def acquireResource(self, pid, rid, requestquantity):
        cursor=self.conn.cursor()
        query = "select r_availability, x.validation from (select validateRequest(request_quantity,r_quantity) as validation from requests natural inner join resource where r_id=%s) as x natural inner join resource where r_id=%s;"
        cursor.execute(query,(rid,rid))
        result = []
        for row in cursor:
            result.append(row)
        if not result:
            return 'No request'
        else:
            availability=result[0][0]
            validation=result[0][1]
            if availability==True and validation==True:
                query = "select r_price from resource where r_id=%s;"
                cursor.execute(query,(rid,))
                result = []
                for row in cursor:
                    result.append(row)
                price=result[0][0]
                if price==0.0:
                    query = "select p_id, r_id from reserves where p_id =%s and r_id=%s;"
                    cursor.execute(query, (pid, rid,))
                    result = []
                    for row in cursor:
                        result.append(row)
                    if result:
                        return 'Reservation done'
                    else:
                        query="insert into reserves(p_id, r_id, resource_total ) values (%s,%s,%s);"
                        cursor.execute(query,(pid,rid,requestquantity,))
                        query="update resource set r_quantity= x.r_quantity-%s from (select r_quantity from resource where r_id=%s) as x where r_id=%s;"
                        cursor.execute(query,(requestquantity,rid,rid))
                        query="select r_quantity from resource where r_id=%s;"
                        cursor.execute(query, (rid,))
                        result = []
                        for row in cursor:
                            result.append(row)
                        quantity = result[0][0]
                        if quantity==0:
                            query = "update resource set r_availability = false where r_id=%s;"
                            cursor.execute(query, (rid,))
                        self.conn.commit()
                        return 'Succeed'
                else:
                    query="select p_id from offers natural inner join payment where p_id=%s and availablepayment = true;"
                    cursor.execute(query,(pid,))
                    result = []
                    for row in cursor:
                        result.append(row)
                    if not result:
                        return 'No payment'
                    else:
                        query="select r_type,r_price from resource where r_id =%s;"
                        cursor.execute(query,(rid,))
                        result = []
                        for row in cursor:
                            result.append(row)
                        rlist = result[0][0]
                        rtotalprice = result[0][1]
                        query = "select payment_id, payment_total from offers natural inner join payment where p_id =%s and availablepayment= true;"
                        cursor.execute(query, (pid,))
                        result = []
                        for row in cursor:
                            result.append(row)
                        payid=result[0][0]
                        paytotal=result[0][1]
                        if paytotal < rtotalprice:
                            return 'Not enough'
                        else:
                            query = "update payment set availablepayment=false where payment_id=%s;"
                            cursor.execute(query, (payid,))
                            query = "select p_id, r_id from offers natural inner join payment natural inner join resource_order natural inner join buys where p_id=%s and r_id=%s;"
                            cursor.execute(query, (pid, rid,))
                            result = []
                            for row in cursor:
                                result.append(row)
                            if result:
                                return 'Purchase done'
                            else:
                                query="insert into resource_order (o_quantity , r_list ,order_total_price ,payment_id ) values ("+requestquantity+",'"+rlist+"',"+str(rtotalprice)+","+str(payid)+") returning o_id;"
                                cursor.execute(query,)
                                result = []
                                for row in cursor:
                                    result.append(row)
                                oid=result[0][0]
                                query="select r_price from resource where r_id=%s;"
                                cursor.execute(query,(rid,))
                                result = []
                                for row in cursor:
                                    result.append(row)
                                rprice=result[0][0]
                                query = "insert into buys(r_id ,o_id ,total_price ,resource_total ) values(%s,"+str(oid)+","+str(rprice)+",%s);"
                                cursor.execute(query,(rid,requestquantity,))
                                query = "update resource set r_quantity= x.r_quantity-%s from (select r_quantity from resource where r_id=%s) as x where r_id=%s;"
                                cursor.execute(query, (requestquantity, rid,rid))
                                query = "select r_quantity from resource where r_id=%s;"
                                cursor.execute(query, (rid,))
                                result = []
                                for row in cursor:
                                    result.append(row)
                                quantity = result[0][0]
                                if quantity == 0:
                                    query = "update resource set r_availability = false where r_id=%s;"
                                    cursor.execute(query, (rid,))
                                self.conn.commit()
                                return 'Succeed'
        self.conn.commit()
        return 'Not available'

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

    def offerPayment(self,pid, payment_type, payment_total):
        cursor = self.conn.cursor()
        query = "insert into payment(payment_type,payment_total, availablepayment) values (%s, %s, true) returning payment_id;"
        cursor.execute(query, (payment_type, payment_total,))
        result = []
        for row in cursor:
            result.append(row)
        payment_id = result[0][0]
        query = "insert into offers(p_id,payment_id) values (%s, %s);"
        cursor.execute(query, (pid,payment_id,))
        self.conn.commit()
        return "New payment"
