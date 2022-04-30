from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Session

from app.models.user_model import UserModel


@jwt_required()
def delete_user():
    session: Session = current_app.db.session
    email = get_jwt_identity()
    user: UserModel = UserModel.query.filter_by(email=email).first()

    session.delete(user)
    session.commit()

    return '', HTTPStatus.NO_CONTENT
