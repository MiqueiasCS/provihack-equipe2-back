import re

from marshmallow import Schema, ValidationError, fields, post_load, validates

from app.models.user_model import UserModel


class RegisterUserSchema(Schema):
    name = fields.String(required=True)
    cpf = fields.String(required=True)
    phone = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)

    @validates('phone')
    def validate_phone(self, value):
        regex = r'(\(\d{2}\))(\d{5}\-\d{4})'

        phone = re.fullmatch(regex, value)

        if not phone:
            raise ValidationError(
                'Telefone obrigatoriamente no formato (xx)xxxxx-xxxx'
            )

    @validates('cpf')
    def validate_cpf(self, value):
        regex = r'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}'

        cpf = re.fullmatch(regex, value)

        if not cpf:
            raise ValidationError('Cpf no formato errado')

    @post_load
    def create_user(self, data, **kwargs):
        return UserModel(**data)


class LoginUserSchema(Schema):
    password = fields.String(required=True)
    email = fields.Email(required=True)
