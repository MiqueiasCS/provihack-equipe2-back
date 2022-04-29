from http import HTTPStatus
from flask import jsonify,current_app

from flask_jwt_extended import jwt_required,get_jwt_identity

from app.models.residue_model import ResidueModel
from app.models.company_model import CompanyModel

import re

from app.services.exceptions import Invalid_uuid_error, Not_found_item_error,Unauthorized_erro


def is_valid_uuid(uuid):
    regex_uuid = "(^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$)"

    uuid_is_valid = re.fullmatch(regex_uuid, uuid,re.I)

    if not uuid_is_valid:
        raise Invalid_uuid_error

    return uuid_is_valid


def update_company(residue,company_email,session):
    company:CompanyModel = CompanyModel.query.filter_by(email=company_email).first()

    if not company:
        raise Unauthorized_erro("Somente uma empresa cadastrada pode acessar esta rota")

    company.quantity_collect += residue.quantity
    # session.add(company)
    # session.commit()

    return company


def update_residue(uuid,session):
    residue:ResidueModel = ResidueModel.query.get(uuid)

    if not residue:
        raise Not_found_item_error("O residuo não foi encontrado")
    
    residue.collected = True
    
    # session.add(residue)
    # session.commit()

    return residue


@jwt_required()
def collect_residue(uuid):
    session = current_app.db.session

    company_email = get_jwt_identity()
    try:
        is_valid_uuid(uuid)
   
        residue = update_residue(uuid,session)
        
        company = update_company(residue,company_email,session)

        session.add(residue)
        session.add(company)
        session.commit()

        # company:CompanyModel = CompanyModel.query.filter_by(email=company_email).first()

        # company.quantity_collect += residue.quantity
        # session.add(company)
        return "",HTTPStatus.OK

    except Invalid_uuid_error as err:
        return {"message":err.message }, HTTPStatus.BAD_REQUEST
    except Not_found_item_error as err:
        return {"message": err.message},HTTPStatus.NOT_FOUND
    except Unauthorized_erro as err:
        return {"message": err.message},HTTPStatus.UNAUTHORIZED