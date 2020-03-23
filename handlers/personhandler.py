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

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_type'] = row[1]
        result['r_quantity'] = row[2]
        result['r_location'] = row[3]
        result['r_price'] = row[4]
        result['r_availability'] = row[5]
        return result

    def getAllPerson(self):
        dao = PersonDAO()
        person_list = dao.getAllPerson()
        #person1 = (1,'Yetsiel','S','Aviles','yetsiel.aviles@upr.edu','Hormigueros','1','7877877878',4)
        #person2 = (2,'Tito','M','Kayak','titokayak@gmail.com','San Juan','2','9399399393',5)
        #person_list = {person1, person2}
        result_list = []
        for row in person_list:
            result = self.build_person_dict(row)
            result_list.append(result)
        return jsonify(PersonList=result_list)

    def getPersonById(self, pid):

        #person1 = (1, 'Yetsiel', 'S', 'Aviles', 'yetsiel.aviles@upr.edu', 'Hormigueros', '1', '7877877878',4)
        dao = PersonDAO()
        person1 = dao.getPersonById(pid)
        if not person1:
            return jsonify(Error="Person Not Found"), 404
        else:
            person = self.build_person_dict(person1)
        return jsonify(Person=person)

    def getResourcesByPersonId(self, pid):
        #person1 = (1, 'Yetsiel', 'S', 'Aviles', 'yetsiel.aviles@upr.edu', 'Hormigueros', '1', '7877877878',4)
        #resource1= (1,'Ice',1,'Mayaguez',1.0,True)
        #resource2= (2,'Batteries',5,'Mayaguez',5.0,True)
        #resources_list ={resource1,resource2}
        dao = PersonDAO()
        person1 = dao.getPersonById(pid)
        if not person1:
            return jsonify(Error="Person Not Found"), 404
        resources_list = dao.getResourcesByPersonId(pid)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(ResourcesByPersonID=result_list)

    def searchPerson(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location_of_p")
            if location:
                #person1 = (1, 'Yetsiel', 'S', 'Aviles', 'yetsiel.aviles@upr.edu', 'Hormigueros', '1', '7877877878',4)
                #person2 = (2, 'Tito', 'M', 'Kayak', 'titokayak@gmail.com', 'San Juan', '2', '9399399393',5)
                #person_list = {person1, person2}
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
                #row = (1, 'Yetsiel', 'S', 'Aviles', 'yetsiel.aviles@upr.edu', 'Hormigueros', '7877877878',4)
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
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def deletePart(self, pid):
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