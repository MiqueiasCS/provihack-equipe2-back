from uuid import uuid4

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    point = Column(Integer, nullable=False, default=0)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    @property
    def password(self):
        raise AttributeError('Password is not accessible')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = UserModel
        load_instance = True

    id = auto_field()
    name = auto_field()
    email = auto_field()
    cpf = auto_field()
    point = auto_field()
    phone = auto_field()
