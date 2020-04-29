from flask import jsonify
from dao.login import LoginDAO
class LoginHandler:
    def build_login_dict(self, row):
        result = {}
        result['login_id'] = row[0]
        result['username'] = row[1]
        result['password'] = row[2]
        return result


    def getAllLogin(self):
        dao = LoginDAO()
        login_list = dao.getAllLogin()
        result_list = []
        for row in login_list:
            result = self.build_login_dict(row)
            result_list.append(result)
        return jsonify(LoginList=result_list)

    def getLoginById(self, login_id):
        dao = LoginDAO()
        login = dao.getLoginById(login_id)
        if not login:
            return jsonify(Error="Login Not Found"), 404
        else:
            login = self.build_login_dict(login)
        return jsonify(Login=login)

    def insertLogin(self, form):
        if form and len(form) == 2:
            username = form['username']
            password = form['password']

            if username and password:
                dao = LoginDAO()
                login_id = dao.insertLogin(username, password)
                result = {}
                result['login_id'] = login_id
                result['username'] = username
                result['password'] = password
                return jsonify(Login=result), 201
            else:
                return jsonify('Unexpected attributes in post request'), 401
        else:
            return jsonify(Error="Malformed post request"), 400


    def deleteLogin(self, login_id):
        dao = LoginDAO()
        login = dao.getLoginById(login_id)
        if not login:
            return jsonify(Error="Login Not Found"), 404
        dao.deleteLogin(login_id)
        return jsonify(DeleteStatus = "OK"), 200

    def updateLogin(self, login_id, form):
        dao = LoginDAO()
        login = dao.getLoginById(login_id)
        if not login:
            return jsonify(Error="Login Not Found"), 404
        if len(form) != 2:
            return jsonify(Error="Malformed update request"), 400
        else:
            username = form['username']
            password = form['password']
            if username and password:
                dao.updateLogin(login_id, username, password)
                result = {}
                result['login_id'] = login_id
                result['username'] = username
                result['password'] = password
                return jsonify(Login=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400
