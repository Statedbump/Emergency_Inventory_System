from flask import Flask, jsonify, request, render_template
from handlers.personhandler import PersonHandler
from handlers.supplierhandler import supplierHandler
from handlers.administratorhandler import AdministratorHandler
from handlers.resources import ResourcesHandler
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
    else :
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
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/ERIApp/person/<int:p_id>/resources')
def getResourcesByPersonId(p_id):
    return PersonHandler().getResourcesByPersonId(p_id)


#------Supplier--------
@app.route('/ERIApp/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return supplierHandler().insertSupplier(request.form)
    else :
        if not request.args:
            return supplierHandler().getAllSuppliers()
        else:
            return supplierHandler().searchSupplier(request.args)

@app.route('/ERIApp/suppliers/<int:p_id>',
           methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(p_id):
    if request.method == 'GET':
        return supplierHandler().getSupplierById(p_id)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/ERIApp/suppliers/<int:p_id>/resources')
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