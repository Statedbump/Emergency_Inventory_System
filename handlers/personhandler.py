from flask import jsonify
from dao.person import PersonDAO
class PersonHandler:

    def build_person_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['first_name'] = row[1]
        result['middle_initial'] = row[2]
        result['last_name'] = row[3]
        result['email'] = row[4]
        result['location_of_p'] = row[5]
        result['phone'] = row[6]
        result['login_id'] = row[7]
        return result

    def build_requested_resource_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['first_name'] = row[1]
        result['middle_initial'] = row[2]
        result['last_name'] = row[3]
        result['r_id'] = row[4]
        result['r_type'] = row[5]
        result['r_location'] = row[6]
        result['r_quantity'] = row[7]
        if result['r_type'] == 'Water':
            result['water_type'] = row[8]
            result['measurement_unit'] = row[9]
            result['r_availability'] = row[10]
        elif result['r_type'] == 'Fuel':
            result['fuel_type'] = row[8]
            result['fuel_octane_rating'] = row[9]
            result['r_availability'] = row[10]
        elif result['r_type'] == 'Food':
            result['food_type'] = row[8]
            result['r_availability'] = row[9]
        else:
            result['r_availability'] = row[8]
        return result

    def build_reserved_and_purchased_resource_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['first_name'] = row[1]
        result['middle_initial'] = row[2]
        result['last_name'] = row[3]
        result['r_id'] = row[4]
        result['r_type'] = row[5]
        if result['r_type'] == 'Water':
            result['water_type'] = row[6]
            result['measurement_unit'] = row[7]
            result['resource_total'] = row[8]
            result['date'] = row[9]
        elif result['r_type'] == 'Fuel':
            result['fuel_type'] = row[6]
            result['fuel_octane_rating'] = row[7]
            result['resource_total'] = row[8]
            result['date'] = row[9]
        elif result['r_type'] == 'Food':
            result['food_type'] = row[6]
            result['resource_total'] = row[7]
            result['date'] = row[8]
        else:
            result['resource_total'] = row[6]
            result['date'] = row[7]
        return result

    def getAllPerson(self):
        dao = PersonDAO()
        person_list = dao.getAllPerson()
        result_list = []
        for row in person_list:
            result = self.build_person_dict(row)
            result_list.append(result)
        return jsonify(PersonList=result_list)

    def getPersonById(self, pid):
        dao = PersonDAO()
        person1 = dao.getPersonById(pid)
        if not person1:
            return jsonify(Error="Person Not Found"), 404
        else:
            person = self.build_person_dict(person1)
        return jsonify(Person=person)

    def getPersonByLocation(self, location):
        dao = PersonDAO()
        person_list = dao.getPersonByLocation(location)
        if not person_list:
            return jsonify(Error="Person Not Found"), 404
        else:
            result_list = []
            for row in person_list:
                result = self.build_person_dict(row)
                result_list.append(result)
            return jsonify(PersonList=result_list)

    def getReservedResourcesByPersonId(self, pid):
        dao = PersonDAO()
        person1 = dao.getPersonById(pid)
        if not person1:
            return jsonify(Error="Person Not Found"), 404
        resources_list = dao.getReservedResourcesByPersonId(pid)
        result_list = []
        for row in resources_list:
            result = self.build_reserved_and_purchased_resource_dict(row)
            result_list.append(result)
        return jsonify(ReservedResourcesByPersonID=result_list)

    def getPurchasedResourcesByPersonId(self, pid):
        dao = PersonDAO()
        person1 = dao.getPersonById(pid)
        if not person1:
            return jsonify(Error="Person Not Found"), 404
        resources_list = dao.getPurchasedResourcesByPersonId(pid)
        result_list = []
        for row in resources_list:
            result = self.build_reserved_and_purchased_resource_dict(row)
            result_list.append(result)
        return jsonify(PurchasedResourcesByPersonID=result_list)

    def getRequestedResourcesByPersonId(self, p_id):
        dao = PersonDAO()
        person1 = dao.getPersonById(p_id)
        if not person1:
            return jsonify(Error="Person Not Found"), 404
        resources_list = dao.getRequestedResourcesByPersonId(p_id)
        result_list = []
        for row in resources_list:
            result = self.build_requested_resource_dict(row)
            result_list.append(result)
        return jsonify(RequestedResourcesByPersonID=result_list)


    def searchPerson(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location_of_p")
            if location:
                dao = PersonDAO()
                person_list = dao.getPersonByLocation(location)
                result_list = []
                for row in person_list:
                    result = self.build_person_dict(row)
                    result_list.append(row)
                return jsonify(PersonList=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertPerson(self, form):
        if form and len(form) == 7:
            pfirstname = form['first_name']
            pmiddleinitial = form['middle_initial']
            plastname = form['last_name']
            email = form['email']
            plocation = form['location_of_p']
            pphone = form['phone']
            loginID = form['login_id']
            if pfirstname and plastname and pmiddleinitial and pphone and loginID and plocation and email:
                dao = PersonDAO()
                pid = dao.insert(pfirstname, pmiddleinitial, plastname, email, plocation, pphone, loginID)
                result = {}
                result['p_id'] = pid
                result['first_name'] = pfirstname
                result['middle_initial'] = pmiddleinitial
                result['last_name'] = plastname
                result['email'] = email
                result['location_of_p'] = plocation
                result['phone'] = pphone
                result['login_id'] = loginID
                return jsonify(Person=result), 201
            else:
                return jsonify('Unexpected attributes in post request'), 401
        else:
            return jsonify(Error="Malformed post request"), 400


    def deletePerson(self, pid):
        dao = PersonDAO()
        if not dao.getPersonById(pid):
            return jsonify(Error = "Person not found."), 404
        else:
            dao.delete(pid)
            return jsonify(DeleteStatus = "OK"), 200

    def updatePerson(self, pid, form):
        dao = PersonDAO()
        if not dao.getPersonById(pid):
            return jsonify(Error = "Person not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                pfirstname = form['first_name']
                pmiddleinitial = form['middle_initial']
                plastname = form['last_name']
                email = form['email']
                plocation = form['location_of_p']
                pphone = form['phone']
                loginID = form['login_id']
                if pfirstname and plastname and pmiddleinitial and pphone and loginID and plocation and email:
                    dao.update(pid, pfirstname, pmiddleinitial, plastname, email, plocation, pphone, loginID)
                    result = {}
                    result['p_id'] = pid
                    result['first_name'] = pfirstname
                    result['middle_initial'] = pmiddleinitial
                    result['last_name'] = plastname
                    result['email'] = email
                    result['location_of_p'] = plocation
                    result['phone'] = pphone
                    result['login_id'] = loginID
                    return jsonify(Person=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def requestResource(self, pid, form):
        dao = PersonDAO()
        if not dao.getPersonById(pid):
            return jsonify(Error="Person not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                rid = form['r_id']
                requestquantity = form['request_quantity']
                if rid and requestquantity:
                    dao.requestResource(pid, rid, requestquantity)
                    result = {}
                    result['p_id'] = pid
                    result['r_id'] = rid
                    result['request_quantity'] = requestquantity
                    return jsonify(Request=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in insert request"), 400