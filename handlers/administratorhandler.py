from flask import jsonify
class AdministratorHandler:
    def build_admin_dict(self, row):
        result = {}
        result['adm_id'] = row[0]
        result['permission_key'] = row[1]
        result['p_id'] = row[2]

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

    def getAllAdmin(self):
        adm1 = (1, 'Permiso', 1)
        adm2 = (2, 'Permiso', 2)
        administrators_list = {adm1, adm2}
        result_list = []
        for row in administrators_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(AdministratorList=result_list)

    def getAdminByAdmId(self, admid):
        admin1 = (1, 'Permiso', 1)
        admin = self.build_admin_dict(admin1)
        return jsonify(Admin=admin)

    def getResourcesByAdminId(self, admid):
        admin1 = (1, 'permiso', 1)
        resource1 = (1, 'Ice', 1, 'Mayaguez', 1.0, True)
        resource2 = (2, 'Batteries', 5, 'Mayaguez', 5.0, True)
        resources_list = {resource1, resource2}
        if not admin1:
            return jsonify(Error="Admin Not Found"), 404
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(ResourcesByAdminID=result_list)

    def searchAdmin(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location_of_p")
            if location:
                admin1 = (1, 'Andres', 1)
                admin2 = (2, 'Andres', 2)
                admin_list = {admin1, admin2}
                result_list = []
                for row in admin_list:
                    result = self.build_admin_dict(row)
                    result_list.append(row)
                return jsonify(AdminList=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400
