from http import HTTPStatus

from flask import current_app,jsonify,request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.company_model import CompanySchema
from app.schemas.company_schemas import RegisterCompanySchema

def register_company():
    register_schema = RegisterCompanySchema()
    company_schema = CompanySchema()

    try:
        session = current_app.db.session
        data = request.get_json()
        new_company = register_schema.load(data)

        session.add(new_company)
        session.commit()

        return company_schema.dump(new_company), HTTPStatus.CREATED
    except IntegrityError as err:
        if 'psycopg2.errors.UniqueViolation' in str(err):
            return jsonify(erro='Company já cadastrada!'),HTTPStatus.CONFLICT
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST