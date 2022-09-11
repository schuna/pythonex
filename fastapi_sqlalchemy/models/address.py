from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel


class AddressDto(BaseModel):
    email_address: str


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(80), nullable=True)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="addresses", lazy='joined')

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r}"
