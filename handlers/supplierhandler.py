from flask import jsonify
from dao.supplier import SupplierDAO

class supplierHandler:

    def build_supplier_dict(self, row):
        result = {}
        result['supplier_id'] = row[0]
        result['first_name'] = row[1]
        result['middle_initial'] = row[2]
        result['last_name'] = row[3]
        result['company_name'] = row[4]
        result['warehouse_address'] = row[5]
        result['supplier_location'] = row[6]
        result['phone'] = row[7]
        result['login_id'] = row[8]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['supplier_id'] = row[0]
        result['first_name'] = row[1]
        result['middle_initial'] = row[2]
        result['last_name'] = row[3]
        result['r_id'] = row[4]
        result['r_type'] = row[5]
        if result['r_type'] == 'Water':
            result['water_type'] = row[6]
            result['measurement_unit'] = row[7]
            result['r_location'] = row[8]
            result['supply_date']= row[9]
        elif result['r_type'] == 'Fuel':
            result['fuel_type'] = row[6]
            result['fuel_octane_rating'] = row[7]
            result['r_location'] = row[8]
            result['supply_date'] = row[9]
        elif result['r_type'] == 'Food':
            result['food_type'] = row[6]
            result['r_location'] = row[7]
            result['supply_date'] = row[8]
        else:
            result['r_location'] = row[6]
            result['supply_date'] = row[7]
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(SupplierList=result_list)

    def getSupplierById(self, sid):
        dao = SupplierDAO()
        sup1 = dao.getSupplierById(sid)
        if not sup1:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            supplier = self.build_supplier_dict(sup1)
        return jsonify(Supplier = supplier)

    def getSupplierByLocation(self, location):
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
            location = args.get("supplier_location")
            if location:
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
            sfirstname = form['first_name']
            smiddleinitial = form['middle_initial']
            slastname = form['last_name']
            companyname = form['company_name']
            warehouseaddress = form['warehouse_address']
            slocation = form['supplier_location']
            sphone = form['phone']
            loginID = form['login_id']
            if sfirstname and slastname and smiddleinitial and companyname and warehouseaddress and slocation and sphone and loginID:
                dao = SupplierDAO()
                sid = dao.insert(sfirstname, smiddleinitial, slastname, slocation, companyname, warehouseaddress, sphone, loginID)
                result = {}
                result['s_id'] = sid
                result['first_name'] = sfirstname
                result['middle_initial'] = smiddleinitial
                result['last_name'] = slastname
                result['company_name'] = companyname
                result['warehouse_address'] = warehouseaddress
                result['supplier_location'] = slocation
                result['phone'] = sphone
                result['login_id'] = loginID
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request.")
        else:
            return jsonify(Error="Malformed post request."), 400

    def deleteSupplier(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier not found."), 404
        else:
            dao.delete(sid)
            return jsonify(DeleteStatus="OK"), 200

    def updateSupplier(self, sid, form):
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
                companyname = form['company_name']
                warehouseaddress = form['warehouse_address']
                slocation = form['supplier_location']
                sphone = form['phone']
                loginID = form['login_id']
                if sfirstname and smiddleinitial and slastname and slocation and companyname and warehouseaddress and sphone and loginID:
                    dao.update(sid, sfirstname, smiddleinitial, slastname, slocation, companyname, warehouseaddress, sphone, loginID)
                    result = {}
                    result['s_id'] = sid
                    result['first_name'] = sfirstname
                    result['middle_initial'] = smiddleinitial
                    result['last_name'] = slastname
                    result['company_name'] = companyname
                    result['warehouse_address'] = warehouseaddress
                    result['supplier_location'] = slocation
                    result['phone'] = sphone
                    result['login_id'] = loginID
                    return jsonify(Supplier=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400