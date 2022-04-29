from uuid import uuid4

from marshmallow_sqlalchemy import SQLAlchemySchema,auto_field
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
    quantity_collect = Column(String, nullable=False,default=0)

    @property
    def password(self):
        raise AttributeError('Password is not accessible')

    @password.setter
    def password(self,password_to_hash):
        self.password_hash=generate_password_hash(password_to_hash)

    def check_password(self,password_to_compare):
        return check_password_hash(self.password_hash,password_to_compare)

class CompanySchema(SQLAlchemySchema):
    class Meta:
        model = CompanyModel
        load_instance = True

    id = auto_field()
    name= auto_field()
    email = auto_field()
    cnpj = auto_field()
    phone = auto_field()
    quantity_collect= auto_field()

