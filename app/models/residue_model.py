from uuid import uuid4
from dataclasses import dataclass

from sqlalchemy import Column, Float, Boolean,String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from app.configs.database import db


@dataclass
class ResidueModel(db.Model):
    type:str
    quantity: float
    collected: bool

    __tablename__ = 'residues'

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid4)
    type = Column(String, nullable=False)
    quantity = Column(Float, nullable = False)
    collected = Column(Boolean, default= False)

    user_id = Column(UUID(as_uuid=True),ForeignKey('users.id', ondelete='CASCADE'))

    user = relationship("UserModel", backref=backref("residues",uselist=True),uselist=False)


    def serialize(self):
        return {
            "id":self.id,
            "type":self.type,
            "quantity": self.quantity,
            "collected": self.collected,
            "user": self.user        }

    
class ResidueSchema(SQLAlchemySchema):
    class Meta:
        model = ResidueModel
        load_instance = True

    id = auto_field()
    type = auto_field()
    quantity = auto_field()
    collected = auto_field()
    user = auto_field()
    
