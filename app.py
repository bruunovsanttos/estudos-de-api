from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


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
    }

]
class Hoteis(Resource):
    def get(self):
        return {'hoteis':'meus hoteis'}

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/hoteis

