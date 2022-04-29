from http import HTTPStatus
from flask import jsonify,current_app

from flask_jwt_extended import jwt_required,get_jwt_identity

from app.models.residue_model import ResidueModel
from app.models.company_model import CompanyModel

import re


def is_valid_uuid(uuid):
    regex_uuid = "(^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$)"

    uuid_is_valid = re.fullmatch(regex_uuid, uuid,re.I)

    return uuid_is_valid

def update_company():
    ...


def update_residue():
    ...


@jwt_required()
def collect_residue(uuid):
    session = current_app.db.session
    company_email = get_jwt_identity()

    if not is_valid_uuid(uuid):
        return {"message":"O id do resíduo passado por parâmetro deve ser do formato uuid v4"}, HTTPStatus.BAD_REQUEST
    
    residue:ResidueModel = ResidueModel.query.get(uuid)
    residue.collected = True

    if not residue:
        return {"message":"O residuo não foi encontrado"},HTTPStatus.NOT_FOUND
    
    session.add(residue)
    session.commit()

    company:CompanyModel = CompanyModel.query.filter_by(email=company_email).first()

    company.quantity_collect += residue.quantity
    session.add(company)
    session.commit()

    return jsonify(residue),HTTPStatus.OK

    