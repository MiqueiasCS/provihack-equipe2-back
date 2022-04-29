from http import HTTPStatus

from flask import current_app, request
from flask_jwt_extended import  get_jwt_identity, jwt_required

from app.models.company_model import CompanyModel

@jwt_required()
def update_user():
    data = request.get_json()
    session = current_app.db.session
    email = get_jwt_identity()
    company = CompanyModel.query.filter_by(email=email).first()

    if 'cnpj' in data:
         if data['cnpj']:
            return {'error':'Não é permitido alterar CNPJ'}, HTTPStatus.UNAUTHORIZED

    for key,value in data.items():
        if key == 'email':
            setattr(company,key,value)
        if key == 'password':
            password_to_hash = data['password']
            company.password = password_to_hash

    session.add(company)
    session.commit()


   

    return '', HTTPStatus.NO_CONTENT