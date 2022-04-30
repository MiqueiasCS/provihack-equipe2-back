from uuid import uuid4

from marshmallow import Schema, fields
from sqlalchemy import Column, Integer,String
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db

class CompanyModel(db.Model):
    __tablename__ = 'company'

    id = Column(UUID(as_uuid=True), primary_key= True, default=uuid4)
    name= Column(String,nullable=False)
    fantsy_name = Column(String) 
    cnpj= Column(String,nullable=False)
    point = Column(String, nullable=False,default=0)
    phone = Column(String,nullable=False)
    email= Column(String,nullable=False)
    password_hash = Column(String, nullable=False)
    ong=Column(String,nullable=False,default=True)
    quantity_collect = Column(Integer, nullable=False,default=0)

    @property
    def password(self):
        raise AttributeError('Password is not accessible')

    @password.setter
    def password(self,password_to_hash):
        self.password_hash=generate_password_hash(password_to_hash)

    def check_password(self,password_to_compare):
        return check_password_hash(self.password_hash,password_to_compare)

class CompanySchema(Schema):
    class Meta:
        ordered = True
        include_relationships = True

    id=fields.Str()
    name= fields.Str()
    cnpj= fields.Str()
    phone = fields.Str()
    email= fields.Str()
    quantity_collect = fields.Integer()
    address = fields.Nested('AddressSchema', many=False)

