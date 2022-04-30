from marshmallow import Schema, fields, post_load

from app.models.residue_model import ResidueModel


class RegisterResidueSchema(Schema):
    type = fields.String(required=True)
    quantity = fields.Float(required=True)
    user_id = fields.UUID(required=True)
    date = fields.DateTime(required=True)

    @post_load
    def create_residue(self, data, **kwargs):
        return ResidueModel(**data)
