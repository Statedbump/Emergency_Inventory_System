from flask import Flask, jsonify, request
from handlers.personhandler import PersonHandler
from handlers.supplierhandler import supplierHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def greetings():
    return 'Welcome to the Emergency Resource Inventory Application!'

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

if __name__ == '__main__':
    app.run()