from http import HTTPStatus

from flask import current_app, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.orm import Session

from flask_jwt_extended.utils import get_jwt_identity
from app.models.user_model import UserModel
from app.schemas.residue_schema import RegisterResidueSchema
from app.models.residue_model import ResidueSchema

def register_residue():
    session: Session = current_app.db.session
    register_schema = RegisterResidueSchema()
    residue_schema = ResidueSchema()

    try:
        user = get_jwt_identity() 

        current_user = UserModel.query.filter_by(email=user).first()
        
        data = request.get_json()
        data["user_id"] = current_user.id

        residue_to_discard = register_schema.load(data)

        session.add(residue_to_discard)
        session.commit()

        # print(residue_to_discard.serialize())
        return jsonify(residue_to_discard.serialize()),200
        # return residue_schema.dump(residue_to_discard),HTTPStatus.OK

    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST