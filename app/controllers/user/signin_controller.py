from http import HTTPStatus

from flask import current_app, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.user_model import UserSchema
from app.schemas.address_schema import CreateAddressSchema
from app.schemas.user_schemas import RegisterUserSchema


def register_user():
    register_schema = RegisterUserSchema()
    user_schema = UserSchema()
    address_schema = CreateAddressSchema()

    try:
        session: Session = current_app.db.session
        data = request.get_json()
        address = {'address': data.pop('address')}

        new_user = register_schema.load(data)
        user_address = address_schema.load(address)

        session.add(new_user)
        session.commit()

        user_address.user_id = new_user.id

        session.add(user_address)
        session.commit()

        return user_schema.dump(new_user), HTTPStatus.CREATED

    except IntegrityError as err:
        if 'psycopg2.errors.UniqueViolation' in str(err):
            return jsonify(erro='Usuário já cadastrado'), HTTPStatus.CONFLICT
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST
