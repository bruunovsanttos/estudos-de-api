from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import create_access_token, jwt_required
import sqlite3

#criação do path para as querys de varios parametros
#contrutor do path
path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str)
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('diaria_max', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)


class Hoteis(Resource):
    def get(self):
        dados = path_params.parse_args()
        {'limit':50, 'diaria_min': None}
        dados['limit']
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        
        return {'hoteis':[hotel.json() for hotel in HotelModel.query.all()]}

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ser deixado em branco.")# deixa campos obrigatórios
    argumentos.add_argument('estrelas', type=float, required=True, help="O campo 'estrelas' não pode ser deixado em branco.")
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')


    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()

        return {'message': 'Hotel not found.'}, 404 #não achado

    @jwt_required()
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"mesage": "Hotel id '{}' already exists.".format(hotel_id)} , 400 #bad request


        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying save hotel.'}, 500 #internal server error
        return hotel.json()

    @jwt_required()
    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()

        hotel_encontrado = HotelModel.find_hotel(hotel_id)

        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)#se não houer um hotel com o nome ele retorna criando um novo hotel
            hotel_encontrado.save_hotel()#salvando no baco de dados
            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()#criando novo hotel se não tem um hotel existente
        except:
            return {
                'message': 'An internal error ocurred trying save hotel.'}, 500  #internal server error
        return hotel.json(), 201 #created (criado novo hotel)

    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An error ocurred trying to delete hotel.'}, 500
            return {'message': 'Hotel deleted'}
        return {'message':'Hotel not found'}, 404