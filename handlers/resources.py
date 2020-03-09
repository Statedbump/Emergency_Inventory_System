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
    def getResourceById(self,r_id):
    def searchResource(self,args):
    def getSupplierByResourceId(self,r_id):

    def insertResource


