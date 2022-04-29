from uuid import uuid4

from sqlalchemy import Column, Float, Boolean,String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
from marshmallow import Schema, fields

from app.configs.database import db



class ResidueModel(db.Model):

    __tablename__ = 'residues'

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid4)
    type = Column(String, nullable=False)
    quantity = Column(Float, nullable = False)
    collected = Column(Boolean, default= False)

    user_id = Column(UUID(as_uuid=True),ForeignKey('users.id', ondelete='CASCADE'))

    user = relationship("UserModel", backref=backref("residues",uselist=True),uselist=False)

    
class ResidueSchema(Schema):
    class Meta:
        model = ResidueModel
        load_instance = True

    id = fields.Str()
    type = fields.Str()
    quantity = fields.Float()
    collected = fields.Bool()
    user = fields.Nested('UserSchema',only=("name", "email","address"),many=False)
    
