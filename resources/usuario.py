from flask_restful import Resource, reqparse
from models.usuario import UserModel

class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()

        return {'message': 'User not found.'}, 404 #não achado

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
        }
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'User deleted'}
        return {'message':'User not found'}, 404

class UserRegister(Resource):
    def post(self):
        atributos = reqparse.RequestParser()
        atributos.add_argument('login', type=str, required=True, help="The Field 'login' cannot be left blank")
        atributos.add_argument('senha', type=str, required=True, help="The Field 'senha' cannot be left blank")
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {f"message": "The login '{}' already exists".format(dados['login'])}

        user = UserModel(**dados)
        user.save_user()
        return {'message': 'User created successfuly'}, 201
