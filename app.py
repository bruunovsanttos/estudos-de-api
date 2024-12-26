from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite: ///banco.db' #cria um banco na raiz do programa
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def banco():
    banco.create_all()



api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    from sql_alchemy import banco #colocando aqui pra ser executado somente se for chamado o APP.py por isso é chamado so aqui.
    banco.init_app(app)
    app.run(debug=True)

    #http://127.0.0.1:5000/hoteis

