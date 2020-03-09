from flask import jsonify
from dao.resources import ResourcesDAO

class ResourcesHandler:
    def build_resource_dict(self,row):
        result = {}
        result['r_id'] = row[0]
        result['r_type'] = row[1]
        result['r_quantity'] = row[2]
        result['r_location'] = row[3]
        result['r_price'] = row[4]
        result['r_availability'] = row[5]
        ##Specializations NEEDED??

    def build_supplier_dict(self,row):
        result = {}
        result['first_name'] = row[0]
        result['middle_initial'] = row[1]
        result['last_name'] = row[2]
        result['company_name'] = row[3]
        result['warehouse_location'] = row[4]
        result['supplier_location'] = row[5]
        result['login_id'] = row[6]
        result['phone'] = row[7]

    def buld_person_dict(self,row):
        result = {}
        result['first_name'] = row[0]
        result['middle_initial'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['location_of_p'] = row[4]
        result['login_id'] = row[5]
        result['phone'] = row[6]

    def build_resource_attributes(self,r_id,r_type,r_quantity,r_location,r_price,r_availability, w_id = NULL,water_type=NULL,measurement_unit=NULL,fuel_id=NULL,fuel_type=NULL,fuel_octane_rating=NULL,food_id=NULL,food_type=NULL):
        result['r_id'] = r_id
        result['r_type'] = r_type
        result['r_quantity'] = r_quantity
        result['r_location'] = r_location
        result['r_price'] = r_price
        result['r_availability'] = r_availability
        if 'water' in r_type:
            result['w_id'] = w_id
            result['water_type'] = water_type
            result['measurement_unit'] = measurement_unit
        elif 'fuel' in r_type:
            result['fuel_id'] = fuel_id
            result['fuel_type']= fuel_type
            result['fuel_octane_rating']=fuel_octane_rating
        elif'food' in r_type:
            result['food_id'] = food_id
            result['food_type'] = food_type
        
        return result

    def getAllResources(self):
        r1=(1,'batteries',10,'San Juan',10.0,TRUE)
        r2=(1,'water',3,'San Juan',4.35,TRUE)

        resource_list = {r1,r2}
        result = []
        for row in person_list:
            result.append(self.build_resource_dict(row))
        return jsonify(ResourceList=result)


        
    def getResourceById(self,r_id):
        r1=(1,'batteries',10,'San Juan',10.0,TRUE) 

        if not r1:
            return jsonify(Eror = 'Resource Not Found'),404
        else:
            r = self.build_resource_dict(r1)
        return jsonify(Resource=r)

    def searchResource(self,args):
        
    def getSupplierByResourceId(self,r_id):
    def getPersonByResourceId(self,r_id):

    def insertResource(self,form):
        if len(form) < 5 or len(form) >8:
            return jsonify(Error = "Malformed pst Request"),400
        else:
            r_type = form['r_type']
            r_quantity = form['r_quantity']
            r_location  = form['r_location']
            r_price = form['r_price']
            r_availability = form['r_availability']
            if 'water' in r_type:
                water_type = form['water_type']
                measurement_unit = form['measurement_unit']
            if 'fuel' in r_type:
                fuel_type = form['fuel_type']
                fuel_octane_rating = form['fuel_octane_rating']
            if 'food' in r_type:
                food_type = form['food_type']
            
            if r_type and r_quantity and r_location and r_price and r_availability:
                if water_type and measurement_unit:
                    result = build_resource_attributes():
                if fuel_type and fuel_octane_rating:
                    result = build_resource_attributes():
                if food_type:
                    result = build_resource_attributes():

                return jsonify(Resource=result),201
            else
                return jsonify('Unexpected attributes in post request'),401
            
    def insertResourceJson(self,json):

        r_type = json['r_type']
        r_quantity = json['r_quantity']
        r_location  = json['r_location']
        r_price = json['r_price']
        r_availability = json['r_availability']
        if 'water' in r_type:
            water_type = json['water_type']
            measurement_unit = json['measurement_unit']
        if 'fuel' in r_type:
            fuel_type = json['fuel_type']
            fuel_octane_rating = json['fuel_octane_rating']
        if 'food' in r_type:
            food_type = json['food_type']
        
        if r_type and r_quantity and r_location and r_price and r_availability:
            if water_type and measurement_unit:
                result = build_resource_attributes():
            if fuel_type and fuel_octane_rating:
                result = build_resource_attributes():
            if food_type:
                result = build_resource_attributes():

            return jsonify(Resource=result),201
        else
            return jsonify('Unexpected attributes in post request'),401 

    



