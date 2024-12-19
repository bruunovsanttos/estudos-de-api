from flask_restful import Resource

hoteis = [
    {
        'hotel_id':'Infinity',
        'nome': 'Infinity Hotel',
        'estrelas': 4.9,
        'diaria': 450.92,
        'cidade': 'São Bernardo do Campo'
    },
    {
        'hotel_id':'Properity',
        'nome': 'Hotel Prosperidade',
        'estrelas': 4.0,
        'diaria': 400.92,
        'cidade': 'Santo André'
    },
    {
        'hotel_id':'Coconut',
        'nome': 'Coco Salgado',
        'estrelas': 3.3,
        'diaria': 289.92,
        'cidade': 'Diadema'
    },
    {
        'hotel_id':'Choque',
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
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
            return {'message': 'Hotel not found.'}, 404 #não achado


    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass