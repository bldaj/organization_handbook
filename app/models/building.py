from sqlalchemy import (
    Column,
    Float,
    Integer,
    String,
)
from sqlalchemy.orm import (
    relationship,
)

from app.db.base import (
    Base,
)


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    organizations = relationship("Organization", back_populates="building")
