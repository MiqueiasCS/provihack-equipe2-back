from http import HTTPStatus

from flask import request
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError
from sqlalchemy.orm import Query

from app.models.user_model import UserModel
from app.schemas.user_schemas import LoginUserSchema


def login_user():
    login_schema = LoginUserSchema()
    user_query: Query = UserModel.query

    try:
        data = request.get_json()
        login_schema.load(data)

        user: UserModel = user_query.filter_by(email=data['email']).first()

        if not user:
            return {
                'error': 'Email ou senha incorretos'
            }, HTTPStatus.UNAUTHORIZED
        if not user.check_password(data['password']):
            return {
                'error': 'Email ou senha incorretos'
            }, HTTPStatus.UNAUTHORIZED

        token = create_access_token(identity=user.email)

        return {'access_token': token}, HTTPStatus.OK

    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST
