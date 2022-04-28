from email.policy import default
from uuid import uuid4


from sqlalchemy import Column, Float, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db

class ResidueModel(db.Model):
    __tablename__ = 'residues'

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid4)
    quantity = Column(Float, nullable = False)
    collected = Column(Boolean, default= False)
