from http import HTTPStatus
from marshmallow import ValidationError
from flask import jsonify

from app.models.company_model import CompanyModel,CompanySchema

def get_all_company():
    company_schema = CompanySchema()

    company = CompanyModel.query.all()
    
    output = []
    for comp in company:
        output.append(company_schema.dump(comp))

    return jsonify(output), HTTPStatus.OK

# def get_district_company():
    #company_schema = CompanySchema()

    #data = request.get_json()

    #district=data['district']

    #company = CompanyModel.query.all()

    #output=[]
    #for comp in company:
        #if comp.address.district == district:
            #output.append(company_schema.dump(comp))

    #return jsonify(output), HTTPStatus.OK

# def get_city_company():
    #company_schema = CompanySchema()

    #data = request.get_json()

    #district=data['city']

    #company = CompanyModel.query.all()

    #output=[]
    #for comp in company:
        #if comp.address.city == city:
            #output.append(company_schema.dump(comp))

    #return jsonify(output), HTTPStatus.OK