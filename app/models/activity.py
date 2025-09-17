from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import (
    relationship,
)

from app.db.base import (
    Base,
)


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    parent_id = Column(Integer, ForeignKey("activities.id"), nullable=True)

    parent = relationship("Activity", remote_side=[id], backref="children")
