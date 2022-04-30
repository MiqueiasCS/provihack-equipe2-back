from uuid import uuid4

from marshmallow import Schema, fields
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


class AddressModel(db.Model):
    __tablename__ = 'address'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    street = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    complement = Column(String, nullable=False)
    state = Column(String, nullable=False)
    cep = Column(String, nullable=False)
    district = Column(String, nullable=False)
    city = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    company_id = Column(UUID(as_uuid=True), ForeignKey('company.id'))

    companies = relationship(
        'CompanyModel',
        backref=backref('address', uselist=False),
        uselist=False,
    )

    users = relationship(
        'UserModel', backref=backref('address', uselist=False), uselist=False
    )

    residues = relationship('ResidueModel', backref='address', uselist=True)


class AddressSchema(Schema):
    class Meta:
        ordered = True
        include_fk = True

    street = fields.Str()
    district = fields.Str()
    city = fields.Str()
    number = fields.Integer()
    complement = fields.Str()
    state = fields.Str()
    cep = fields.Str()
