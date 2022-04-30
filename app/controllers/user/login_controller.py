from http import HTTPStatus

from flask import request
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError
from sqlalchemy.orm import Query

from app.models.company_model import CompanyModel
from app.models.user_model import UserModel
from app.schemas.user_schemas import LoginUserSchema


def login_user():
    login_schema = LoginUserSchema()
    user_query: Query = UserModel.query
    company_query: Query = CompanyModel.query

    try:
        data = request.get_json()
        login_schema.load(data)

        user: UserModel = user_query.filter_by(email=data['email']).first()
        company: CompanyModel = company_query.filter_by(
            email=data['email']
        ).first()
        if not user and not company:
            return {
                'error': 'Email ou senha incorretos'
            }, HTTPStatus.UNAUTHORIZED

        if user and user.check_password(data['password']):
            token = create_access_token(identity=user.email)
        elif company and company.check_password(data['password']):
            token = create_access_token(identity=company.email)
        else:
            return {
                'error': 'Email ou senha incorretos'
            }, HTTPStatus.UNAUTHORIZED

        return {'access_token': token}, HTTPStatus.OK

    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST
