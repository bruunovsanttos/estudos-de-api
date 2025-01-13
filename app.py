from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'banco.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_PATH}' #cria um banco na raiz do programa
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLE'] = True
api = Api(app)
jwt = JWTManager(app)


#@app.before_first_request nas versões atuais do flask não é mais utilizado esse modelo. por isso da erro
# def banco_dados():
#    banco.create_all()



api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin,'/login')
api.add_resource(UserLogout,'/logout')


@jwt.token_in_blocklist_loader
def verifica_blacklist(jwt_header, jwt_payload):
    # Verifica se o 'jti' do token está na blacklist
    return jwt_payload['jti'] in BLACKLIST

# Função para tratar tokens revogados
@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'You have been logged out'}), 401  # Retorna o erro 401 se o token foi revogado

if __name__ == '__main__':
    from sql_alchemy import banco #colocando aqui pra ser executado somente se for chamado o APP.py por isso é chamado so aqui.
    banco.init_app(app)
    with app.app_context():
        banco.create_all()
    #@jwt.token_in_blocklist_loader()
    #def verifica_blacklist(self, token):
    #    return token['jti'] in BLACKLIST
    #@jwt.revoked_token_loader()
    #def token_de_acesso_invalidado(jwt_header, jwt_payload):
    #    return json({'message': 'You have been logged out'}), 401#unatorized



    app.run(debug=True)

    #http://127.0.0.1:5000/hoteis

