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
class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrela': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }



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
        hotel = Hotel.encontrar_hotel(hotel_id)
        if hotel:
            return hotel

        return {'message': 'Hotel not found.'}, 404 #não achado


    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'mesage': 'Hotel id "{}" already exists.'.format(hotel_id)} , 400 #bad request


        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        #novo_hotel = {
        #    'hotel_id': hotel_id,
        #    'nome': dados['nome'],
        #    'estrelas': dados['estrelas'],
        #    'diaria': dados['diaria'],
        #    'cidade': dados['cidade']
        #}

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        novo_hotel = { 'hotel_id': hotel_id, **dados} # **dados desempacota os dados do hotel em forma de chave e valor facilitando a escrita do codigo ao inves de escrever todas as chaves e valores:
            #'nome': dados['nome'],
            # 'estrelas': dados['estrelas'],
            #'diaria': dados['diaria'],
            #'cidade': dados['cidade']
            #isso criando os argumentos em cima no codigo das instancias da classe

        hotel = Hotel.encontrar_hotel(hotel_id)

        if hotel:
            hotel.update(novo_hotel)#se não houer um hotel com o nome ele retorna criando um novo hotel
            return novo_hotel, 200
        hoteis.append(novo_hotel)#criando novo hotel se não tem um hotel existente
        return novo_hotel, 201 #created (criado novo hotel)

    def delete(self, hotel_id):
        global hoteis #pega os dados da lista de hoteis

        hoteis_filtrados = []
        for hotel in hoteis:
            if hotel['hotel_id'] != hotel_id:
                hoteis_filtrados.append(hotel) #adiciona o hotel na lista para deletar hoteis_filtrados[]

        hoteis = hoteis_filtrados
        return {'message': 'Hotel deleted'}