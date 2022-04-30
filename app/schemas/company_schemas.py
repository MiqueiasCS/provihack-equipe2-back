import re

from marshmallow import Schema, ValidationError, fields, post_load, validates

from app.models.company_model import CompanyModel


class RegisterCompanySchema(Schema):
    name = fields.String(required=True)
    cnpj = fields.String(required=True)
    phone = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)

    @validates('cnpj')
    def validate_cnpj(self, value):
        regex = r'(^\d{2}.\d{3}.\d{3}/\d{4}-\d{2}$)'

        cnpj = re.fullmatch(regex, value)

        if not cnpj:
            raise ValidationError('CNPJ no formato inválido')

    @post_load
    def create_user(self, data, **kwargs):
        return CompanyModel(**data)
