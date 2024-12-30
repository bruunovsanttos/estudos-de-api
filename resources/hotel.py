from flask_restful import Resource, reqparse
from models.hotel import HotelModel
hoteis = [
    {
        'hotel_id':'infinity',
        'nome': 'Infinity Hotel',
        'estrelas': 4.9,
        'diaria': 450.92,
        'cidade': 'São Bernardo do Campo'
    },
    {
        'hotel_id':'prosperity',
        'nome': 'Hotel Prosperidade',
        'estrelas': 4.0,
        'diaria': 400.92,
        'cidade': 'Santo André'
    },
    {
        'hotel_id':'coconut',
        'nome': 'Coco Salgado',
        'estrelas': 3.3,
        'diaria': 289.92,
        'cidade': 'Diadema'
    },
    {
        'hotel_id':'choque',
        'nome': 'Choque Radius',
        'estrelas': 3.8,
        'diaria': 305.92,
        'cidade': 'São Bernardo do Campo'
    }

]




class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
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
        hotel.save_hotel()
        return hotel.json()



    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()

        hotel_encontrado = HotelModel.find_hotel(hotel_id)

        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)#se não houer um hotel com o nome ele retorna criando um novo hotel
            hotel_encontrado.save_hotel()#salvando no baco de dados
            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel() #criando novo hotel se não tem um hotel existente
        return hotel.json(), 201 #created (criado novo hotel)

    def delete(self, hotel_id):
        global hoteis #pega os dados da lista de hoteis

        hoteis_filtrados = []
        for hotel in hoteis:
            if hotel['hotel_id'] != hotel_id:
                hoteis_filtrados.append(hotel) #adiciona o hotel na lista para deletar hoteis_filtrados[]

        hoteis = hoteis_filtrados
        return {'message': 'Hotel deleted'}