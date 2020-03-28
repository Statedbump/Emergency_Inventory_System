from flask import jsonify
from dao.supplier import SupplierDAO

class supplierHandler:

    def build_supplier_dict(self, row):
        result = {}
        result['s_id'] = row[0]
        result['s_first_name'] = row[1]
        result['s_middle_initial'] = row[2]
        result['s_last_name'] = row[3]
        result['s_location'] = row[4]
        result['company_name'] = row[5]
        result['warehouse_address'] = row[6]
        result['s_phone'] = row[7]
        result['login_id'] = row[8]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_type'] = row[1]
        result['r_location'] = row[2]
        result['resource_total'] = row[3]
        if result['r_type'] == 'Water':
            result['water_type'] = row[4]
            result['measurement_unit'] = row[5]
        elif result['r_type'] == 'Fuel':
            result['fuel_type'] = row[4]
            result['fuel_octane_rating'] = row[5]
        elif result['r_type'] == 'Food':
            result['food_type'] = row[4]
        return result

    def getAllSuppliers(self):
        #sup1 = (1,'Rex','J','Reyes','Cidra','Rexolutions','Cataño','7877877878',1)
        #sup2 = (2,'Juan','D','Barrio','Cayey','Juan Del Barrio Corp','San Juan','9399399393',2)
        #suppliers_list = {sup1, sup2}
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(SupplierList=result_list)

    def getSupplierById(self, sid):
        #sup1 = (1,'Rex','J','Reyes','Cidra','Rexolutions','Cataño','7877877878',1)
        dao = SupplierDAO()
        sup1 = dao.getSupplierById(sid)
        if not sup1:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            supplier = self.build_supplier_dict(sup1)
        return jsonify(Supplier = supplier)

    def getSupplierByLocation(self, location):
        #sup1 = (1, 'Yetsiel', 'S', 'Aviles', 'yetsiel.aviles@upr.edu', 'Hormigueros', '1', '7877877878',4)
        dao = SupplierDAO()
        supplier_list = dao.getSupplierByLocation(location)
        if not supplier_list:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            result_list = []
            for row in supplier_list:
                result = self.build_supplier_dict(row)
                result_list.append(result)
            return jsonify(SupplierList=result_list)

    def getResourcesBySupplierId(self, sid):
        #sup1 = (1,'Rex','J','Reyes','Cidra','Rexolutions','Cataño','7877877878',1)
        #resource1= (1,'Ice',1,'Mayaguez',1.0,True)
        #resource2= (2,'Batteries',5,'Mayaguez',5.0,True)
        #resources_list ={resource1,resource2}
        dao = SupplierDAO()
        sup1 = dao.getSupplierById(sid)
        if not sup1:
            return jsonify(Error="Supplier Not Found"), 404
        resources_list = dao.getResourcesBySupplierId(sid)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(ResourcesBySupplierID=result_list)

    def searchSupplier(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location_of_p")
            if location:
                #sup1 = (1,'Rex','J','Reyes','Cidra','Rexolutions','Cataño','7877877878',1)
                #sup2 = (2,'Juan','D','Barrio','Cayey','Juan Del Barrio Corp','San Juan','9399399393',2)
                #person_list = {sup1, sup2}
                dao = SupplierDAO()
                supplier_list = dao.getSupplierByLocation(location)
                result_list = []
                for row in supplier_list:
                    result = self.build_supplier_dict(row)
                    result_list.append(row)
                return jsonify(SuppliersList=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertSupplier(self, form):
        if form and len(form) == 8:
            sfirstname = form['s_first_name']
            smiddleinitial = form['s_middle_initial']
            slastname = form['s_last_name']
            slocation = form['s_location']
            companyname = form['company_name']
            warehouseaddress = form['warehouse_address']
            sphone = form['s_phone']
            loginID = form['login_id']
            if sfirstname and slastname and smiddleinitial and slocation\
                    and companyname and warehouseaddress and sphone and loginID:
                row = (1,'Rex','J','Reyes','Cidra','Rexolutions','Cataño','7877877878',1)
                result = {}
                result['p_id'] = row[0]
                result['p_first_name'] = row[1]
                result['p_middle_initial'] = row[2]
                result['p_last_name'] = row[3]
                result['email'] = row[4]
                result['location_of_p'] = row[5]
                result['login_id'] = row[6]
                result['p_phone'] = row[7]
                result['login_id'] = row[8]
                return jsonify(Person=result), 201
            else:
                return jsonify(Error="Malformed post request.")
        else:
            return jsonify(Error="Malformed post request.")

        def deleteSupplier(self, sid):
            dao = SupplierDAO()
            if not dao.getSupplierById(sid):
                return jsonify(Error="Supplier not found."), 404
            else:
                dao.delete(sid)
                return jsonify(DeleteStatus="OK"), 200

        def updatePerson(self, sid, form):
            dao = SupplierDAO()
            if not dao.getSupplierById(sid):
                return jsonify(Error="Supplier not found."), 404
            else:
                if len(form) != 8:
                    return jsonify(Error="Malformed update request"), 400
                else:
                    sfirstname = form['first_name']
                    smiddleinitial = form['middle_initial']
                    slastname = form['last_name']
                    slocation = form['s_location']
                    companyname = form['company_name']
                    warehouseaddress = form['warehouse_address']
                    sphone = form['s_phone']
                    loginID = form['login_id']
                    if sfirstname and smiddleinitial and slastname and slocation and companyname and warehouseaddress and sphone and loginID:
                        dao.update(sid, sfirstname, smiddleinitial, slastname, slocation, companyname, warehouseaddress, sphone, loginID)
                        result = {}
                        result['s_id'] = sid
                        result['first_name'] = sfirstname
                        result['middle_initial'] = smiddleinitial
                        result['last_name'] = slastname
                        result['s_location'] = slocation
                        result['company_name'] = companyname
                        result['warehouse_address'] = warehouseaddress
                        result['s_phone'] = sphone
                        result['login_id'] = loginID
                        return jsonify(Supplier=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update request"), 400