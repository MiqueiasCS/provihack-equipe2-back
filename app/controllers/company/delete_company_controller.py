from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.company_model import CompanyModel


@jwt_required()
def delete_company():
    session = current_app.db.session
    email = get_jwt_identity()
    company = CompanyModel.query.filter_by(email=email).first()

    session.delete(company)
    session.commit()

    return ' ', HTTPStatus.NO_CONTENT
