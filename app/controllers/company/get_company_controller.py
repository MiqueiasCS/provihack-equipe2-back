from http import HTTPStatus

from flask import jsonify, request

from app.models.company_model import CompanyModel, CompanySchema


def get_all_company():
    company_schema = CompanySchema()

    company = CompanyModel.query.all()

    data = request.args.get('district', None)
    print(data)
    if data:
        output = []
        for comp in company:
            if comp.address.district == data:
                output.append(company_schema.dump(comp))

        return jsonify(output), HTTPStatus.OK

    return company_schema.dumps(company, many=True), HTTPStatus.OK


def get_one(id):
    company_schema = CompanySchema()

    company = CompanyModel.query.filter_by(id=id).first()
    print(company)

    return company_schema.dump(company), HTTPStatus.OK
