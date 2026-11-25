#!/usr/bin/python3
"""Map city records and their state references."""

from sqlalchemy import Column, ForeignKey, Integer, String

from model_state import Base


class City(Base):
    """Represent one city belonging to a state."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
