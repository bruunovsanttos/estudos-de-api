from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
import hmac
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The Field 'login' cannot be left blank")
atributos.add_argument('senha', type=str, required=True, help="The Field 'senha' cannot be left blank")

class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()

        return {'message': 'User not found.'}, 404 #não achado

    @jwt_required()
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


class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and hmac.compare_digest(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=str(user.user_id))
            return {'access_token': token_de_acesso}, 200
        return {'message'
                :'The username or password is incorrect.'}, 401

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message':'Logged out succesfully'}, 200