from flask import jsonify
from dao.admin import AdminDAO
class AdministratorHandler:

    def build_admin_dict(self, row):
        result = {}
        result['admin_id'] = row[0]
        result['permission_key'] = row[1]
        result['p_id'] = row[2]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_type'] = row[1]
        result['r_quantity'] = row[2]
        result['r_location'] = row[3]
        if result['r_type'] == 'Water':
            result['water_type'] = row[4]
            result['measurement_unit'] = row[5]
            result['r_availability'] = row[6]
            result['admin_id']= row[7]
        elif result['r_type'] == 'Fuel':
            result['fuel_type'] = row[4]
            result['fuel_octane_rating'] = row[5]
            result['r_availability'] = row[6]
            result['admin_id'] = row[7]
        elif result['r_type'] == 'Food':
            result['food_type'] = row[4]
            result['r_availability'] = row[5]
            result['admin_id'] = row[6]
        else:
            result['r_availability'] = row[4]
            result['admin_id'] = row[5]
        return result

    def getAllAdmin(self):
        dao = AdminDAO()
        admin_list = dao.getAllAdmin()
        result_list = []
        for row in admin_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(AdminList=result_list)

    def getAdminById(self, admin_id):
        dao = AdminDAO()
        admin = dao.getAdminById(admin_id)
        if not admin:
            return jsonify(Error="Admin Not Found"), 404
        else:
            admin = self.build_admin_dict(admin)
        return jsonify(Admin=admin)

    def getResourcesByAdminId(self, admin_id):
        dao = AdminDAO()
        admin1 = dao.getAdminById(admin_id)
        if not admin1:
            return jsonify(Error="Admin Not Found"), 404
        resources_list = dao.getResourcesByAdminId(admin_id)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(ResourcesByAdminID=result_list)

    def insertAdmin(self, form):
        if form and len(form) == 2:
            permission_key = form['permission_key']
            p_id = form['p_id']

            if permission_key and p_id:
                dao = AdminDAO()
                admin_id = dao.insertAdmin(permission_key, p_id)
                result = {}
                result['admin_id'] = admin_id
                result['permission_key'] = permission_key
                result['p_id'] = p_id
                return jsonify(Admin=result), 201
            else:
                return jsonify('Unexpected attributes in post request'), 401
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteAdmin(self, admin_id):
        dao = AdminDAO()
        admin = dao.getAdminById(admin_id)
        if not admin:
            return jsonify(Error="Admin Not Found"), 404
        dao.deleteAdmin(admin_id)
        return jsonify(DeleteStatus="OK"), 200

    def updateAdmin(self, admin_id, form):
        dao =AdminDAO()
        admin = dao.getAdminById(admin_id)
        if not admin:
            return jsonify(Error="Admin Not Found"), 404
        if len(form) != 2:
            return jsonify(Error="Malformed update request"), 400
        else:
            permission_key = form['permission_key']
            p_id = form['p_id']
            if permission_key and p_id:
                dao.updateAdmin(admin_id, permission_key, p_id)
                result = {}
                result['admid_id'] = admin_id
                result['permission_key'] = permission_key
                result['p_id'] = p_id
                return jsonify(Admin=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400

    def manageResource(self, admin_id, form):
        dao = AdminDAO()
        if not dao.getAdminById(admin_id):
            return jsonify(Error="Admin not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                rid = form['r_id']
                if rid:
                    dao.manageResource(admin_id, rid)
                    result = {}
                    result['admin_id'] = admin_id
                    result['r_id'] = rid
                    return jsonify(Manage=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in insert request"), 400