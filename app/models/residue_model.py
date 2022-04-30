from uuid import uuid4

from marshmallow import Schema, fields
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


class ResidueModel(db.Model):

    __tablename__ = 'residues'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    type = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    collected = Column(Boolean, default=False)
    date = Column(DateTime, nullable=False)

    address_id = Column(UUID(as_uuid=True), ForeignKey('address.id'))

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))

    company_id = Column(UUID(as_uuid=True), ForeignKey('company.id'))

    user = relationship(
        'UserModel', backref=backref('residues', uselist=True), uselist=False
    )

    company = relationship(
        'CompanyModel',
        backref=backref('residues', uselist=True),
        uselist=False,
    )


class ResidueSchema(Schema):
    class Meta:
        model = ResidueModel
        load_instance = True
        ordered = True

    id = fields.Str()
    type = fields.Str()
    quantity = fields.Int()
    collected = fields.Bool()
    date = fields.DateTime()
    address = fields.Nested('AddressSchema', many=False)
    user = fields.Nested(
        'UserSchema', only=('name', 'email', 'address'), many=False
    )


class ResidueGetSchema(Schema):
    class Meta:
        model = ResidueModel
        load_instance = True
        ordered = True

    id = fields.Str()
    type = fields.Str()
    quantity = fields.Int()
    collected = fields.Bool()
    date = fields.DateTime()
    address = fields.Nested('AddressSchema', many=False)
    user = fields.Nested('UserSchema', only=('name', 'email'), many=False)
    company = fields.Nested(
        'CompanySchema', only=('name', 'email'), many=False
    )
