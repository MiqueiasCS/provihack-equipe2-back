from uuid import uuid4

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import check_password_hash, generate_password_hash
from marshmallow import Schema, fields


class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    point = Column(Integer, nullable=False, default=0)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    @staticmethod
    def serialize(self):
        ...

    @property
    def password(self):
        raise AttributeError('Password is not accessible')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

class UserSchema(Schema):
    class Meta:
        ordered = True
        include_relationships = True

    name = fields.Str()
    cpf = fields.Str()
    point = fields.Integer()
    phone = fields.Str()
    email =  fields.Str()
    address = fields.Nested('AddressSchema', many=False)