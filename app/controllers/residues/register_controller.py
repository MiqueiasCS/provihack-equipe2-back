from http import HTTPStatus

from flask import current_app, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow import ValidationError
from sqlalchemy.orm import Session

from app.models.residue_model import ResidueSchema
from app.models.user_model import UserModel
from app.schemas.address_schema import CreateAddressSchema
from app.schemas.residue_schema import RegisterResidueSchema


@jwt_required()
def register_residue():
    session: Session = current_app.db.session
    register_schema = RegisterResidueSchema()
    residue_schema = ResidueSchema()
    address_schema = CreateAddressSchema()

    try:
        user = get_jwt_identity()

        current_user: UserModel = UserModel.query.filter_by(email=user).first()

        data = request.get_json()

        address = data.get('address')

        if not address:
            address = current_user.address

        else:
            data.pop('address')

            address = address_schema.load({'address': address})
            session.add(address)
            session.commit()

        data['user_id'] = current_user.id

        residue_to_discard = register_schema.load(data)

        residue_to_discard.address_id = address.id
        session.add(residue_to_discard)
        session.commit()

        return residue_schema.dump(residue_to_discard), HTTPStatus.CREATED

    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST
