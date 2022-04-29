from flask import current_app, request
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from sqlalchemy.orm import Session, Query
from app.models.company_model import CompanyModel
from app.models.user_model import UserModel
from app.schemas.address_schema import UpdateAddressSchema

@jwt_required()
def update_address():
    session: Session = current_app.db.session
    user_query: Query = UserModel.query
    company_query:Query = CompanyModel.query

    update_schema = UpdateAddressSchema()
    data = request.get_json()
    email = get_jwt_identity()

    try:
        update_schema.load(data)

        user: UserModel = user_query.filter_by(email=email).first()
        company: CompanyModel = company_query.filter_by(email=email).first()

        if user:
            user_address = user.address[0]
            for key, value in data.items():
                setattr(user_address, key, value)
        
        if company:
            company_address = company.address[0]
            for key, value in data.items():
                setattr(company_address, key, value)

        session.commit()

        return '', HTTPStatus.NO_CONTENT
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST