from flask import jsonify
#from googlemaps import Client as GoogleMaps
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
        return result

    def build_resources_requests_dict(self,row):
        result = {}
        result['p_id'] = row[0]
        result['r_id'] = row[1]
        result['r_type'] = row[2]
        return result

    def build_resources_available_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_type'] = row[1]
        result['r_availability'] = row[2]
        return result

    def build_resourcesInNeed_by_senate_region_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['r_id'] = row[1]
        result['r_type'] = row[2]
        result['request_quantity'] = row[3]
        result['senate_region'] = row[4]
        return result

    def build_resourcesAvailable_by_senate_region_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_type'] = row[1]
        result['r_quantity'] = row[2]
        result['senate_region'] = row[3]
        return result

    def build_resourcesMatching_by_senate_region_dict(self, row):
        result = {}
        result['r_type'] = row[0]
        result['total_quantity'] = row[1]
        result['senate_region'] = row[2]
        return result


    def build_resourcesInNeed_daily_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['r_id'] = row[1]
        result['r_type'] = row[2]
        result['request_quantity'] = row[3]
        result['current_date'] = row[4]
        return result

    def build_resourcesAvailable_daily_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_type'] = row[1]
        result['r_quantity'] = row[2]
        result['current_date'] = row[3]
        return result

    def build_resourcesMatching_daily_dict(self, row):
        result = {}
        result['r_type'] = row[0]
        result['total_quantity'] = row[1]
        result['current_date'] = row[2]
        return result

    def build_resourcesInNeed_weekly_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['r_id'] = row[1]
        result['r_type'] = row[2]
        result['request_quantity'] = row[3]
        result['date (in last 7 days)'] = row[4]
        return result

    def build_resourcesAvailable_weekly_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_type'] = row[1]
        result['r_quantity'] = row[2]
        result['date (in last 7 days)'] = row[3]
        return result

    def build_resourcesMatching_weekly_dict(self, row):
        result = {}
        result['r_type'] = row[0]
        result['total_quantity'] = row[1]
        result['date (in last 7 days)'] = row[2]
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

    def build_resource_attributes(self,r_id,r_type,r_quantity,r_location,r_price,r_availability,
                                  w_id =None ,water_type=None,measurement_unit=None,fuel_id=None,
                                  fuel_type=None,fuel_octane_rating=None,food_id=None,food_type=None,
                                  batt_id=None,batt_type=None,batt_volts=None,gen_id=None,g_brand=None,
                                  g_fuel_type=None,g_power=None):
        result = {}
        result['r_id'] = r_id
        result['r_type'] = r_type
        result['r_quantity'] = r_quantity
        result['r_location'] = r_location
        result['r_price'] = r_price
        result['r_availability'] = r_availability
        if 'water' in result['r_type']:
            result['w_id'] = w_id
            result['water_type'] = water_type
            result['measurement_unit'] = measurement_unit
            return result
        elif 'fuel' in result['r_type']:
            result['fuel_id'] = fuel_id
            result['fuel_type']= fuel_type
            result['fuel_octane_rating']=fuel_octane_rating
            return result
        elif 'food' in result['r_type']:
            result['food_id'] = food_id
            result['food_type'] = food_type
            return result
        elif 'battery' in result['r_type']:
            result['batt_id'] = batt_id
            result['batt_type']= batt_type
            result['batt_volts']=batt_volts
            return result
        elif 'generator' in result['r_type']:
            result['gen_id'] = gen_id
            result['g_fuel_type']= g_fuel_type
            result['g_brand']=g_brand
            result['g_power'] = g_power
            return result
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllResources()
        result_list =[]
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(ResourceList=result_list)

    def getAllResourcesRequests(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllResourcesRequests()
        result_list=[]
        for row in resource_list:
            result = self.build_resources_requests_dict(row)
            result_list.append(result)
        return jsonify(ResourcesRequests= result_list)

    def getAllResourcesAvailable(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllResourcesAvailable()
        result_list = []
        for row in resource_list:
            result = self.build_resources_available_dict(row)
            result_list.append(result)
        return jsonify(ResourcesAvailable=result_list)

    def sortResourcesRequestsByResourceName(self):
        dao = ResourcesDAO()
        resource_list = dao.sortResourcesRequestsByResourceName()
        result_list = []
        for row in resource_list:
            result = self.build_resources_requests_dict(row)
            result_list.append(result)
        return jsonify(SortResourcesRequestsByResourceName=result_list)

    def sortResourcesAvailableByResourceName(self):
        dao = ResourcesDAO()
        resource_list = dao.sortResourcesAvailableByResourceName()
        result_list = []
        for row in resource_list:
            result = self.build_resources_available_dict(row)
            result_list.append(result)
        return jsonify(SortResourcesAvailableByResourceName=result_list)


    def getResourcesInNeedBySenateRegion(self):
        dao = ResourcesDAO()
        resource_list = dao.getResourcesInNeedBySenateRegion()
        result_list = []
        for row in resource_list:
            result = self.build_resourcesInNeed_by_senate_region_dict(row)
            result_list.append(result)
        return jsonify(ResourcesInNeedBySenateRegion=result_list)

    def getResourcesAvailableBySenateRegion(self):
        dao = ResourcesDAO()
        resource_list = dao.getResourcesAvailableBySenateRegion()
        result_list = []
        for row in resource_list:
            result = self.build_resourcesAvailable_by_senate_region_dict(row)
            result_list.append(result)
        return jsonify(ResourcesAvailableBySenateRegion=result_list)

    def getResourcesMatchingBySenateRegion(self):
        dao = ResourcesDAO()
        need_list = dao.getCountResourcesInNeedBySenateRegion()
        result1_list = []
        for row in need_list:
            result = self.build_resourcesMatching_by_senate_region_dict(row)
            result1_list.append(result)

        available_list = dao.getCountResourcesAvailableBySenateRegion()
        result2_list = []
        for row in available_list:
            result = self.build_resourcesMatching_by_senate_region_dict(row)
            result2_list.append(result)
        final_list = {}
        final_list['resources_in_need_by_senate_region'] = result1_list
        final_list['resources_available_by_senate_region'] = result2_list
        return jsonify(ResourcesMatchingBySenateRegion=final_list)

    def getResourcesAvailableDaily(self):
        dao = ResourcesDAO()
        resource_list = dao.getResourcesAvailableDaily()
        result_list = []
        for row in resource_list:
            result = self.build_resourcesAvailable_daily_dict(row)
            result_list.append(result)
        return jsonify(ResourcesAvailableDaily=result_list)

    def getResourcesInNeedDaily(self):
        dao = ResourcesDAO()
        resource_list = dao.getResourcesInNeedDaily()
        result_list = []
        for row in resource_list:
            result = self.build_resourcesInNeed_daily_dict(row)
            result_list.append(result)
        return jsonify(ResourcesInNeedDaily=result_list)

    def getResourcesMatchingDaily(self):
        dao = ResourcesDAO()
        need_list = dao.getCountResourcesInNeedDaily()
        result1_list = []
        for row in need_list:
            result = self.build_resourcesMatching_daily_dict(row)
            result1_list.append(result)

        available_list = dao.getCountResourcesAvailableDaily()
        result2_list = []
        for row in available_list:
            result = self.build_resourcesMatching_daily_dict(row)
            result2_list.append(result)
        final_list = {}
        final_list['resources_in_need_daily'] = result1_list
        final_list['resources_available_daily'] = result2_list
        return jsonify(ResourcesMatchingDaily=final_list)

    def getResourcesInNeedWeekly(self):
        dao = ResourcesDAO()
        resource_list = dao.getResourcesInNeedWeekly()
        result_list = []
        for row in resource_list:
            result = self.build_resourcesInNeed_weekly_dict(row)
            result_list.append(result)
        return jsonify(ResourcesInNeedWeekly=result_list)

    def getResourcesAvailableWeekly(self):
        dao = ResourcesDAO()
        resource_list = dao.getResourcesAvailableWeekly()
        result_list = []
        for row in resource_list:
            result = self.build_resourcesAvailable_weekly_dict(row)
            result_list.append(result)
        return jsonify(ResourcesAvailableWeekly=result_list)

    def getResourcesMatchingWeekly(self):
        dao = ResourcesDAO()
        need_list = dao.getCountResourcesInNeedWeekly()
        result1_list = []
        for row in need_list:
            result = self.build_resourcesMatching_weekly_dict(row)
            result1_list.append(result)

        available_list = dao.getCountResourcesAvailableWeekly()
        result2_list = []
        for row in available_list:
            result = self.build_resourcesMatching_weekly_dict(row)
            result2_list.append(result)
        final_list = {}
        final_list['resources_in_need_weekly'] = result1_list
        final_list['resources_available_weekly'] = result2_list
        return jsonify(ResourcesMatchingWeekly=final_list)
    def getLocationByResourceId(self, r_id):
            dao = ResourcesDAO()
            location = dao.getLocationByResourceId(r_id)
            if not location:
                return jsonify(Error = 'Resource Not Found'),404
            result = location[0][0]
            return result



    def getResourceById(self,r_id):
        dao = ResourcesDAO()
        row = dao.getResourceById(r_id)
        if not row:
            return jsonify(Eror = 'Resource Not Found'),404
        else:
            r = self.build_resource_dict(row)
        return jsonify(Resource=r)


    def searchResource(self,args):
        r_type = args.get('r_type')
        r_availability = args.get('r_availability')
        r_location = args.get('r_location')
        dao = ResourcesDAO()

        resource_list = []
        
        if(len(args)== 3) and r_type and r_availability  and r_location:
           resource_list = dao.getResourcesByTypeLocationAndAvaliability(r_type,r_location,r_availability)

        elif(len(args)== 2) and r_type and r_availability :
           resource_list = dao.getResourcesByTypeAndAvaliability(r_type,r_availability)
        
        elif(len(args)== 2) and r_type and r_location :
           resource_list = dao.getResourcesByTypeAndLocation(r_type,r_location)

        elif(len(args)== 2) and r_availability and r_location :
            resource_list = dao.getResourcesByLocationAndAvailability(r_location,r_availability)

        elif(len(args)== 1) and r_type:
            resource_list = dao.getResourceByType(r_type)
          
        elif(len(args) ==1 ) and r_availability:
            resource_list = dao.getResourceByAvailability(r_availability)

        elif(len(args) ==1 ) and r_location:
            resource_list = dao.getResourceByLocation(r_location)
            
        else:
            return jsonify(Error = "Malformed query string"), 400
        
        result =[]
        for row in resource_list:
            result.append(self.build_resource_dict(row))
        return jsonify(ResourceList=result)

# Needs to be finished
    def getSuppliersByResourceId(self,r_id):
        dao = ResourcesDAO()
        resource = dao.getResourceById(r_id)
        if not resource:
            return jsonify(Error="Resource Not Found"), 404

        result_list = []
        supplier_list = dao.getSupplierByResourceId(r_id)
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(SupplierByResourcesID=result_list)


    #Fix insert
    def insertResource(self,form):
        if len(form) < 5 or len(form) >8:
            return jsonify(Error = "Malformed pst Request"),400
        else:
            r_type = form['r_type']
            r_quantity = form['r_quantity']
            r_location = form['r_location']
            r_price = form['r_price']
            r_availability = form['r_availability']
            if r_type and r_quantity and r_location and r_price and r_availability:
                dao = ResourcesDAO()
                r_id = dao.insertResource(r_type, r_quantity, r_location, r_price, r_availability)
                result = self.build_resource_attributes(r_id, r_type, r_quantity, r_location, r_price, r_availability)
                if 'water' in r_type:
                    water_type = form['water_type']
                    measurement_unit = form['measurement_unit']
                    w_id = dao.insertWater(water_type, measurement_unit,r_id)
                    water = {}
                    water['r_id'] = r_id
                    water['r_type'] = r_type
                    water['r_quantity'] = r_quantity
                    water['r_location'] = r_location
                    water['r_price'] = r_price
                    water['r_availability'] = r_availability
                    water['w_id'] = w_id
                    water['water_type'] = water_type
                    water['measurement_unit'] = measurement_unit
                    return jsonify(Water=water), 201
                if 'fuel' in r_type:
                    fuel_type = form['fuel_type']
                    fuel_octane_rating = form['fuel_octane_rating']
                    fuel_id = dao.insertFuel(fuel_type, fuel_octane_rating,r_id)
                    fuel = {}
                    fuel['r_id'] = r_id
                    fuel['r_type'] = r_type
                    fuel['r_quantity'] = r_quantity
                    fuel['r_location'] = r_location
                    fuel['r_price'] = r_price
                    fuel['r_availability'] = r_availability
                    fuel['fuel_id'] = fuel_id
                    fuel['fuel_octane_rating'] = fuel_octane_rating
                    fuel['fuel_type'] = fuel_type
                    return jsonify(Fuel=fuel), 201
                if 'food' in r_type:
                    food_type = form['food_type']
                    food_id = dao.insertFood(food_type, r_id)
                    food= {}
                    food['r_id'] = r_id
                    food['r_type'] = r_type
                    food['r_quantity'] = r_quantity
                    food['r_location'] = r_location
                    food['r_price'] = r_price
                    food['r_availability'] = r_availability
                    food['food_id'] = food_id
                    food['food_type'] = food_type
                    return jsonify(Food=food), 201
                if 'battery' in r_type:
                    batt_type = form['batt_type']
                    batt_volts = form['batt_volts']
                    batt_id = dao.insertBattery(batt_type, batt_volts, r_id)
                    batt = {}
                    batt['r_id'] = r_id
                    batt['r_type'] = r_type
                    batt['r_quantity'] = r_quantity
                    batt['r_location'] = r_location
                    batt['r_price'] = r_price
                    batt['r_availability'] = r_availability
                    batt['batt_id'] = batt_id
                    batt['batt_type'] = batt_type
                    batt['batt_volts'] = batt_volts
                    return jsonify(Battery=batt), 201
                if 'generator' in r_type:
                    g_brand = form['g_brand']
                    g_fuel_type = form['g_fuel_type']
                    g_power = form['g_power']
                    gen_id = dao.insertGenerator(g_brand,g_fuel_type, g_power, r_id)
                    gen = {}
                    gen['r_id'] = r_id
                    gen['r_type'] = r_type
                    gen['r_quantity'] = r_quantity
                    gen['r_location'] = r_location
                    gen['r_price'] = r_price
                    gen['r_availability'] = r_availability
                    gen['gen_id'] = gen_id
                    gen['g_brand'] = g_brand
                    gen['g_fuel_type'] = g_fuel_type
                    gen['g_power'] = g_power
                    return jsonify(Generator=gen), 201
                else:
                    return jsonify(Resource=result), 201
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

    def getAllResourcesPurchases(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllResourcesPurchases()
        result_list = []
        for row in resource_list:
            result = self.build_resources_requests_dict(row)
            result_list.append(result)
        return jsonify(ResourcesPurchases=result_list)

    def getAllResourcesReserves(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllResourcesReserves()
        result_list = []
        for row in resource_list:
            result = self.build_resources_requests_dict(row)
            result_list.append(result)
        return jsonify(ResourcesReserves=result_list)

    def updateResource(self, r_id, form):
        dao = ResourcesDAO()
        if not dao.getResourceById(r_id):
            return jsonify(Error="Resource not found."), 404
        else:
            if len(form) < 5 or len(form) > 8:
                return jsonify(Error="Malformed pst Request"), 400
            else:
                r_type = form['r_type']
                r_quantity = form['r_quantity']
                r_location = form['r_location']
                r_price = form['r_price']
                r_availability = form['r_availability']
                if r_type and r_quantity and r_location and r_price and r_availability:
                    if 'water' in r_type:
                        water_type = form['water_type']
                        measurement_unit = form['measurement_unit']
                        dao.updateResource(r_id, r_type, r_quantity, r_location, r_price,r_availability)
                        dao.updateWater(water_type, measurement_unit, r_id)
                        result={}
                        result['r_id'] = r_id
                        result['r_type'] = r_type
                        result['r_quantity'] = r_quantity
                        result['r_location'] = r_location
                        result['r_price'] = r_price
                        result['r_availability'] = r_availability
                        result['water_type'] = water_type
                        result['measurement_unit'] = measurement_unit
                        return jsonify(Water=result), 200
                    if 'fuel' in r_type:
                        fuel_type = form['fuel_type']
                        fuel_octane_rating = form['fuel_octane_rating']
                        dao.updateResource(r_id, r_type, r_quantity, r_location, r_price,r_availability)
                        dao.updateFuel( fuel_type, fuel_octane_rating, r_id)
                        result = {}
                        result['r_id'] = r_id
                        result['r_type'] = r_type
                        result['r_quantity'] = r_quantity
                        result['r_location'] = r_location
                        result['r_price'] = r_price
                        result['r_availability'] = r_availability
                        result['fuel_type'] = fuel_type
                        result['fuel_octane_rating'] = fuel_octane_rating
                        return jsonify(Fuel=result), 200
                    if 'food' in r_type:
                        food_type = form['food_type']
                        dao.updateResource(r_id, r_type, r_quantity, r_location, r_price,r_availability)
                        dao.updateFood(food_type, r_id)
                        result = {}
                        result['r_id'] = r_id
                        result['r_type'] = r_type
                        result['r_quantity'] = r_quantity
                        result['r_location'] = r_location
                        result['r_price'] = r_price
                        result['r_availability'] = r_availability
                        result['food_type'] = food_type
                        return jsonify(Food=result), 200
                    if 'battery' in r_type:
                        batt_type = form['batt_type']
                        batt_volts = form['batt_volts']
                        dao.updateResource(r_id, r_type, r_quantity, r_location, r_price,r_availability)
                        dao.updateBattery(batt_type, batt_volts, r_id)
                        result = {}
                        result['r_id'] = r_id
                        result['r_type'] = r_type
                        result['r_quantity'] = r_quantity
                        result['r_location'] = r_location
                        result['r_price'] = r_price
                        result['r_availability'] = r_availability
                        result['batt_type'] = batt_type
                        result['batt_volts'] = batt_volts
                        return jsonify(Battery=result), 200
                    if 'generator' in r_type:
                        g_brand = form['g_brand']
                        g_fuel_type = form['g_fuel_type']
                        g_power = form['g_power']
                        dao.updateResource(r_id, r_type, r_quantity, r_location, r_price,r_availability)
                        dao.updateGenerator(g_brand,g_fuel_type, g_power, r_id)
                        result = {}
                        result['r_id'] = r_id
                        result['r_type'] = r_type
                        result['r_quantity'] = r_quantity
                        result['r_location'] = r_location
                        result['r_price'] = r_price
                        result['r_availability'] = r_availability
                        result['g_brand'] = g_brand
                        result['g_fuel_type'] = g_fuel_type
                        result['g_power'] = g_power
                        return jsonify(Generator=result), 200
                    else:
                        dao.updateResource(r_id,r_type, r_quantity, r_location, r_price, r_availability)
                        result = {}
                        result['r_id'] = r_id
                        result['r_type'] = r_type
                        result['r_quantity'] = r_quantity
                        result['r_location'] = r_location
                        result['r_price'] = r_price
                        result['r_availability'] = r_availability
                        return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteResource(self, r_id):
        dao = ResourcesDAO()
        if not dao.getResourceById(r_id):
            return jsonify(Error="Resource not found."), 404
        else:
            dao.deleteResource(r_id)
            return jsonify(DeleteStatus="OK"), 200



