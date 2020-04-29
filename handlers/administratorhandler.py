from flask import jsonify
from dao.admin import AdminDAO
class AdministratorHandler:
    def build_admin_dict(self, row):
        result = {}
        result['admin_id'] = row[0]
        result['permission_key'] = row[1]
        result['p_id'] = row[2]
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
