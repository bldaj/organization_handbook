from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
)
from sqlalchemy.orm import (
    relationship,
)

from app.db.base import (
    Base,
)


# Ассоциативная таблица для many-to-many Организация <-> Деятельность
organization_activity = Table(
    "organization_activity",
    Base.metadata,
    Column("organization_id", ForeignKey("organizations.id"), primary_key=True),
    Column("activity_id", ForeignKey("activities.id"), primary_key=True),
)


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    building_id = Column(Integer, ForeignKey("buildings.id"), nullable=False)

    building = relationship("Building", back_populates="organizations")
    phones = relationship("OrganizationPhone", back_populates="organization", cascade="all, delete-orphan")
    activities = relationship("Activity", secondary=organization_activity, backref="organizations")


class OrganizationPhone(Base):
    __tablename__ = "organization_phones"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)

    organization = relationship("Organization", back_populates="phones")
