from http import HTTPStatus

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from psycopg2 import IntegrityError

from app.models.user_model import UserModel


@jwt_required()
def update_user():
    data = request.get_json()
    session = current_app.db.session
    email = get_jwt_identity()
    user: UserModel = UserModel.query.filter_by(email=email).first()
    try:
        for key, value in data.items():
            if key == 'name':
                setattr(user, key, value)
            if key == 'email':
                setattr(user, key, value)
            if key == 'point':
                setattr(user, key, value)
            if key == 'phone':
                setattr(user, key, value)
            if key == 'password':
                password_to_hash = data['password']
                user.password = password_to_hash

        session.add(user)
        session.commit()

        return '', HTTPStatus.NO_CONTENT
    except IntegrityError as err:
        if 'psycopg2.errors.UniqueViolation' in str(err):
            return jsonify(erro='Usuário já cadastrado!'),HTTPStatus.CONFLICT