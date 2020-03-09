from flask import jsonify
class PersonHandler:
    def build_person_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['p_first_name'] = row[1]
        result['p_middle_initial'] = row[2]
        result['p_last_name'] = row[3]
        result['email'] = row[4]
        result['location_of_p'] = row[5]
        result['login_id'] = row[6]
        result['p_phone'] = row[7]

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

    def getAllPerson(self):

        person1 = (1,'Yetsiel','S','Aviles','yetsiel.aviles@upr.edu','Hormigueros','1','7877877878')
        person2 = (2,'Tito','M','Kayak','titokayak@gmail.com','San Juan','2','9399399393')
        person_list = {person1,person2}
        result_list = []
        for row in person_list:
            result = self.build_person_dict(row)
            result_list.append(result)
        return jsonify(PersonList=result_list)

    def getPersonById(self, pid):

        person1 = (1, 'Yetsiel', 'S', 'Aviles', 'yetsiel.aviles@upr.edu', 'Hormigueros', '1', '7877877878')
        if not person1:
            return jsonify(Error="Person Not Found"), 404
        else:
            person = self.build_person_dict(person1)
        return jsonify(Person=person)

    def getResourcesByPersonId(self, pid):
        person1 = (1, 'Yetsiel', 'S', 'Aviles', 'yetsiel.aviles@upr.edu', 'Hormigueros', '1', '7877877878')
        resource1= (1,'Ice',1,'Mayaguez',1.0,True)
        resource2= (2,'Batteries',5,'Mayaguez',5.0,True)
        resources_list ={resource1,resource2}
        if not person1:
            return jsonify(Error="Person Not Found"), 404

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
                person1 = (1, 'Yetsiel', 'S', 'Aviles', 'yetsiel.aviles@upr.edu', 'Hormigueros', '1', '7877877878')
                person2 = (2, 'Tito', 'M', 'Kayak', 'titokayak@gmail.com', 'San Juan', '2', '9399399393')
                person_list = {person1, person2}
                result_list = []
                for row in person_list:
                    result = self.build_person_dict(row)
                    result_list.append(row)
                return jsonify(PersonList=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertPerson(self, form):
        if form and len(form) == 7:
            pfirstname = form['p_first_name']
            pmiddleinitial = form['p_middle_initial']
            plastname = form['p_last_name']
            email = form['email']
            plocation = form['location_of_p']
            plogin = form['login_id']
            pphone = form['p_phone']
            if pfirstname and plastname and pmiddleinitial and pphone and plogin and plocation and email:
                row = (1, 'Yetsiel', 'S', 'Aviles', 'yetsiel.aviles@upr.edu', 'Hormigueros', '1', '7877877878')
                result = {}
                result['p_id'] = row[0]
                result['p_first_name'] = row[1]
                result['p_middle_initial'] = row[2]
                result['p_last_name'] = row[3]
                result['email'] = row[4]
                result['location_of_p'] = row[5]
                result['login_id'] = row[6]
                result['p_phone'] = row[7]
                return jsonify(Person=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")