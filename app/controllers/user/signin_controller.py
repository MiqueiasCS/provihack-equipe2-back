from http import HTTPStatus

from flask import current_app, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.user_model import UserSchema
from app.schemas.user_schemas import RegisterUserSchema


def register_user():
    register_schema = RegisterUserSchema()
    user_schema = UserSchema()

    try:
        session: Session = current_app.db.session
        data = request.get_json()
        new_user = register_schema.load(data)

        session.add(new_user)
        session.commit()

        return user_schema.dump(new_user), HTTPStatus.CREATED

    except IntegrityError as err:
        if 'psycopg2.errors.UniqueViolation' in str(err):
            return jsonify(erro='Usuário já cadastrado'), HTTPStatus.CONFLICT
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST
