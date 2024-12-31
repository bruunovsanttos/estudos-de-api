from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return {'hoteis':[hotel.json() for hotel in HotelModel.query.all()]}

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True)# deixa campos obrigatórios
    argumentos.add_argument('estrelas', type=float, required=True)
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')


    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()

        return {'message': 'Hotel not found.'}, 404 #não achado


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

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An error ocurred trying to delete hotel.'}, 500
            return {'message': 'Hotel deleted'}
        return {'message':'Hotel not found'}, 404