from flask import jsonify
class LoginHandler:
    def build_login_dict(self, row):
        result = {}
        result['username'] = row[0]
        result['password'] = row[1]
        return result

    def getAllLogin(self):
        login1 = ('josemelendez35', 'YHLQMDLG')
        login2 = ('rex', 'dinosaurio')
        login_list = {login1, login2}
        result_list = []
        for row in login_list:
            result = self.build_login_dict(row)
            result_list.append(result)
        return jsonify(LoginList=result_list)

