from flask_restful import Resource, reqparse

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

    def encontrar_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None
    def get(self, hotel_id):
        hotel = Hotel.encontrar_hotel(hotel_id)
        if hotel:
            return hotel

        return {'message': 'Hotel not found.'}, 404 #não achado


    def post(self, hotel_id):


        dados = Hotel.argumentos.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }

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
        pass