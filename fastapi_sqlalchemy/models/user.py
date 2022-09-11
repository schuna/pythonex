from typing import Optional

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base
from pydantic import BaseModel

from models.address import AddressDto


class UserDto(BaseModel):
    name: str
    fullname: str
    addresses: Optional[list[AddressDto]] = None


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(80))

    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan", lazy='joined'
    )

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}"
