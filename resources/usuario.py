from flask_restful import Resource, reqparse
from models.usuario import UserModel

class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()

        return {'message': 'Hotel not found.'}, 404 #não achado

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An error ocurred trying to delete hotel.'}, 500
            return {'message': 'Hotel deleted'}
        return {'message':'Hotel not found'}, 404