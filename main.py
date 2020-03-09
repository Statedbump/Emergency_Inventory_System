from flask import Flask, jsonify, request
from handlers.personhandler import PersonHandler
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
    return 'Hello, this is the Emergency Resource Inventory DB App!'

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


if __name__ == '__main__':
    app.run()
