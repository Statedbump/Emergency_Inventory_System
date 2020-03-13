from flask import jsonify

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
        result['p_phone'] = row[7]
        result['login_id'] = row[8]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['resource_type'] = row[1]
        result['quantity'] = row[2]
        result['res_location'] = row[3]
        result['r_price'] = row[4]
        result['r_availability'] = row[5]
        return result

    def getAllSuppliers(self):
        sup1 = (1,'Rex','J','Reyes','Cidra','Rexolutions','Cataño','7877877878',1)
        sup2 = (2,'Juan','D','Barrio','Cayey','Juan Del Barrio Corp','San Juan','9399399393',2)
        suppliers_list = {sup1, sup2}
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(PersonList=result_list)

    def getSupplierById(self, pid):
        sup1 = (1,'Rex','J','Reyes','Cidra','Rexolutions','Cataño','7877877878',1)
        if not sup1:
            return jsonify(Error="Person Not Found"), 404
        else:
            person = self.build_supplier_dict(sup1)
        return jsonify(Person=person)

    def getResourcesBySupplierId(self, pid):
        sup1 = (1,'Rex','J','Reyes','Cidra','Rexolutions','Cataño','7877877878',1)
        resource1= (1,'Ice',1,'Mayaguez',1.0,True)
        resource2= (2,'Batteries',5,'Mayaguez',5.0,True)
        resources_list ={resource1,resource2}
        if not sup1:
            return jsonify(Error="Person Not Found"), 404
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
                sup1 = (1,'Rex','J','Reyes','Cidra','Rexolutions','Cataño','7877877878',1)
                sup2 = (2,'Juan','D','Barrio','Cayey','Juan Del Barrio Corp','San Juan','9399399393',2)
                person_list = {sup1, sup2}
                result_list = []
                for row in person_list:
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
            pphone = form['p_phone']
            loginID = form['login_id']
            if sfirstname and slastname and smiddleinitial and slocation\
                    and companyname and warehouseaddress and pphone and loginID:
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