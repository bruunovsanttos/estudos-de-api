from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' #cria um banco na raiz do programa
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

#@app.before_first_request nas versões atuais do flask não é mais utilizado esse modelo. por isso da erro
# def banco_dados():
#    banco.create_all()

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, 'usuarios/<int:user_id>')

if __name__ == '__main__':
    from sql_alchemy import banco #colocando aqui pra ser executado somente se for chamado o APP.py por isso é chamado so aqui.
    banco.init_app(app)
    with app.app_context():
        banco.create_all()

    app.run(debug=True)

    #http://127.0.0.1:5000/hoteis

