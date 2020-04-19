from flask import Flask, jsonify, request, render_template
from handlers.personhandler import PersonHandler
from handlers.supplierhandler import supplierHandler
from handlers.administratorhandler import AdministratorHandler
from handlers.resourcehandler import ResourcesHandler
from handlers.loginhandler import LoginHandler

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/ERIApp/home')
def landing():
    return render_template("home.html")

@app.route('/ERIApp/signup')
def signup():
    return render_template("signup.html")



#-----Person------
@app.route('/ERIApp/person', methods=['GET', 'POST'])
def getAllPerson():
    if request.method == 'POST':
        return PersonHandler().insertPerson(request.form)
    else:
        if not request.args:
            return PersonHandler().getAllPerson()
        else:
            return PersonHandler().searchPerson(request.args)

@app.route('/ERIApp/person/<int:p_id>',
           methods=['GET', 'PUT', 'DELETE'])
def getPersonById(p_id):
    if request.method == 'GET':
        return PersonHandler().getPersonById(p_id)
    elif request.method == 'PUT':
        return PersonHandler().updatePerson(p_id, request.form)
    elif request.method == 'DELETE':
        return PersonHandler().deletePerson(p_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/ERIApp/person/<int:p_id>/resources')
def getResourcesByPersonId(p_id):
    return PersonHandler().getResourcesByPersonId(p_id)


@app.route('/ERIApp/person/<int:p_id>/requests')
def getRequestedResourcesByPersonId(p_id):
    return PersonHandler().getRequestedResourcesByPersonId(p_id)



#------Supplier--------
@app.route('/ERIApp/supplier', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return supplierHandler().insertSupplier(request.form)
    else :
        if not request.args:
            return supplierHandler().getAllSuppliers()
        else:
            return supplierHandler().searchSupplier(request.args)

@app.route('/ERIApp/supplier/<int:s_id>',
           methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(s_id):
    if request.method == 'GET':
        return supplierHandler().getSupplierById(s_id)
    elif request.method == 'PUT':
        return supplierHandler().updateSupplier(s_id, request.form)
    elif request.method == 'DELETE':
        return supplierHandler().deleteSupplier(s_id)
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/ERIApp/supplier/<int:p_id>/resources')
def getResourcesBySupplierId(p_id):
    return supplierHandler().getResourcesBySupplierId(p_id)



#-----Admin------
@app.route('/ERIApp/administrators')
def getAllAdmin():
    return AdministratorHandler().getAllAdmin()

@app.route('/ERIApp/administrators/<int:adm_id>')
def getAdminByAdmId(adm_id):
    return AdministratorHandler().getAdminByAdmId(adm_id)

@app.route('/ERIApp/administrators/<int:adm_id>/resources')
def getResourcesByAdminId(adm_id):
    return AdministratorHandler().getResourcesByAdminId(adm_id)



#---------------Login-------------------
@app.route('/ERIApp/login')
def getAllLogin():
    return LoginHandler().getAllLogin()



#----->Resources<-----
@app.route('/ERIApp/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        return ResourcesHandler().insertResource(request.form)
    else :
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().searchResource(request.args)

@app.route('/ERIApp/resources/requests', methods=['GET'])
def getAllResourcesRequests():
    return ResourcesHandler().getAllResourcesRequests()

@app.route('/ERIApp/resources/requests/SortByResourceName', methods=['GET'])
def sortResourcesRequestsByResourceName():
    return ResourcesHandler().sortResourcesRequestsByResourceName()

@app.route('/ERIApp/resources/available', methods=['GET'])
def getAllResourcesAvailable():
    return ResourcesHandler().getAllResourcesAvailable()

@app.route('/ERIApp/resources/available/SortByResourceName', methods=['GET'])
def sortResourcesAvailableByResourceName():
    return ResourcesHandler().sortResourcesAvailableByResourceName()

@app.route('/ERIApp/resources/NeedBySenateRegion', methods=['GET'])
def getResourcesInNeedBySenateRegion():
    return ResourcesHandler().getResourcesInNeedBySenateRegion()

@app.route('/ERIApp/resources/AvailableBySenateRegion', methods=['GET'])
def getResourcesAvailableBySenateRegion():
    return ResourcesHandler().getResourcesAvailableBySenateRegion()

@app.route('/ERIApp/resources/MatchingBySenateRegion', methods=['GET'])
def getResourcesMatchingBySenateRegion():
    return ResourcesHandler().getResourcesMatchingBySenateRegion()

@app.route('/ERIApp/resources/NeedDaily', methods=['GET'])
def getResourcesInNeedDaily():
    return ResourcesHandler().getResourcesInNeedDaily()

@app.route('/ERIApp/resources/AvailableDaily', methods=['GET'])
def getResourcesAvailableDaily():
    return ResourcesHandler().getResourcesAvailableDaily()

@app.route('/ERIApp/resources/MatchingDaily', methods=['GET'])
def getResourcesMatchingDaily():
    return ResourcesHandler().getResourcesMatchingByDaily()

@app.route('/ERIApp/resources/<int:r_id>',
           methods=['GET', 'PUT', 'DELETE'])
def getResourceById(r_id):
    if request.method == 'GET':
        return ResourcesHandler().getResourceById(r_id)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/ERIApp/resources/<int:r_id>/person')
def getPersonByResourceId(r_id):
    return ResourcesHandler().getPersonByResourceId(r_id)

@app.route('/ERIApp/resources/<int:r_id>/supplier')
def getSupplierByResourceId(r_id):
    return ResourcesHandler().getSuppliersByResourceId(r_id) 



if __name__ == '__main__':
    app.run(debug=True)