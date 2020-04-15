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

    def build_resources_by_senate_region_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_type'] = row[1]
        result['senate_region'] = row[2]
        return result


        ##Specializations NEEDED??

    def build_supplier_dict(self, row):
        result = {}
        result['s_id'] = row[0]
        result['s_first_name'] = row[1]
        result['s_middle_initial'] = row[2]
        result['s_last_name'] = row[3]
        result['s_location'] = row[4]
        result['company_name'] = row[5]
        result['warehouse_address'] = row[6]
        result['p_phone'] = row[7]
        result['login_id'] = row[8]
        return result

    def build_person_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['p_first_name'] = row[1]
        result['p_middle_initial'] = row[2]
        result['p_last_name'] = row[3]
        result['email'] = row[4]
        result['location_of_p'] = row[5]
        result['p_phone'] = row[6]
        result['login_id'] = row[7]
        return result

    def build_resource_attributes(self,r_id,r_type,r_quantity,r_location,r_price,r_availability, w_id =None ,water_type=None,measurement_unit=None,fuel_id=None,fuel_type=None,fuel_octane_rating=None,food_id=None,food_type=None):
        result = {}
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
        r1=(1,'batteries',10,'San Juan',10.0,True)
        r2=(1,'water',3,'San Juan',4.35,True)

        resource_list = {r1,r2}
        result_list =[]
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(ResourceList=result_list)

    def getResourcesInNeedBySenateRegion(self):
        dao = ResourcesDAO()
        resource_list = dao.getResourcesInNeedBySenateRegion()
        result_list = []
        for row in resource_list:
            result = self.build_resources_by_senate_region_dict(row)
            result_list.append(result)
        return jsonify(ResourcesInNeedBySenateRegion=result_list)

    def getResourcesAvailableBySenateRegion(self):
        dao = ResourcesDAO()
        resource_list = dao.getResourcesAvailableBySenateRegion()
        result_list = []
        for row in resource_list:
            result = self.build_resources_by_senate_region_dict(row)
            result_list.append(result)
        return jsonify(ResourcesAvailableBySenateRegion=result_list)
        
    def getResourceById(self,r_id):
        r1=(1,'batteries',10,'San Juan',10.0,True) 

        if not r1:
            return jsonify(Eror = 'Resource Not Found'),404
        else:
            r = self.build_resource_dict(r1)
        return jsonify(Resource=r)

    def searchResource(self,args):
        r_type = args.get('r_type')
        r_availability = args.get('r_availability')
        r_location = args.get('r_location')
        
        if(len(args)== 2) and r_type and r_availability:
            r1=(1,'water',2,'San Juan',5.0,True)
            r2=(1,'water',1,'San Juan',4.35,True)

        elif(len(args)== 1) and r_type:
            r1=(1,'batteries',10,'San Juan',10.0,True)
            r2=(1,'batteries',3,'San Juan',4.35,True)
        elif(len(args) ==1 ) and r_availability:
            r1=(1,'batteries',10,'San Juan',10.0,True)
            r2=(1,'water',3,'San Juan',4.35,True)

        elif(len(args) ==1 ) and r_location:
            r1=(1,'batteries',10,'San Juan',10.0,True)
            r2=(1,'water',3,'San Juan',4.35,True)
        else:
            return jsonify(Error = "Malformed query string"), 400
        resource_list = {r1,r2}
        result =[]
        for row in resource_list:
            result.append(self.build_resource_dict(row))
        return jsonify(ResourceList=result)


        
        
    def getSuppliersByResourceId(self,r_id):
        sup1 = (1, 'Luke', 'O', 'Skywalker', 'Rebels Inc', '102 RebelBase 31', 'Tatoine','777-127-8789',1)
        sup2 = (1, 'Leia', 'P', 'Skywalker', 'Rebels Inc', '102 RebelBase 31', 'Quorosant','777-127-8889' ,1)
        resource = (2,'Batteries',5,'Mayaguez',5.0,True)
        supplier_list = {sup1,sup2}
        if not resource:
            return jsonify(Error="Resource Not Found"), 404

        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(SupplierByResourcesID=result_list)


    def getPersonByResourceId(self,r_id):
        p1 = (1,'Joe','F','Chill','joe.chill@upr.edu','Jayuyas','7877787811',1)
        p2 = (2,'Tito','M','Kayak','titokayak@gmail.com','San Juan','9399399393',2)
        resource = (2,'Batteries',5,'Mayaguez',5.0,True)

        person_list = {p1,p2}
        if not resource:
            return jsonify(Error="Resource Not Found"), 404

        result_list = []
        for row in person_list:
            result = self.buld_person_dict(row)
            result_list.append(result)
        return jsonify(PersonByResourcesID=result_list)


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
                    result = self.build_resource_attributes()
                if fuel_type and fuel_octane_rating:
                    result = self.build_resource_attributes()
                if food_type:
                    result = self.build_resource_attributes()

                return jsonify(Resource=result),201
            else:
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
                result = self.build_resource_attributes()
            if fuel_type and fuel_octane_rating:
                result = self.build_resource_attributes()
            if food_type:
                result = self.build_resource_attributes()

            return jsonify(Resource=result),201
        else:
            return jsonify('Unexpected attributes in post request'),401 

    



