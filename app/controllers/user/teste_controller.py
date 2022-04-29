from flask import request
from marshmallow import ValidationError
from app.models.user_model import UserModel, UserSchema



def teste():
    user_schema = UserSchema()

    data = request.get_json()

    email = data['email']

    user: UserModel = UserModel.query.filter_by(email=email).first()
    
    

    return user_schema.dump(user), 200