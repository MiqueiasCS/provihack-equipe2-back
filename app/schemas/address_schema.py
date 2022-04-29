
from app.models.address_model import AddressModel
from marshmallow import Schema, fields, post_load

AddressSchema = Schema.from_dict(
    {
        "street": fields.String(required=True),
        "district": fields.String(required=True),
        "city": fields.String(required=True),
        "number": fields.Integer(required=True),
        "complement": fields.String(required=True),
        "state": fields.String(required=True),
        "cep": fields.String(required=True)
    }
)

class CreateAddressSchema(Schema):
    address = fields.Nested(AddressSchema, required=True)
    
    @post_load
    def create_address(self, data, **kwargs):
        return AddressModel(**data['address'])


class UpdateAddressSchema(Schema):
    street = fields.String(required=True)
    district = fields.String(required=True)
    city = fields.String(required=True)
    number = fields.Integer(required=True)
    complement = fields.String(required=True)
    state = fields.String(required=True)
    cep = fields.String(required=True)