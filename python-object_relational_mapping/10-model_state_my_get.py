#!/usr/bin/python3
"""Print the ID of a state found by its name."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session

from model_state import Base, State


if __name__ == "__main__":
    url = URL.create("mysql+mysqldb", username=sys.argv[1],
                     password=sys.argv[2], host="localhost", port=3306,
                     database=sys.argv[3])
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        state = session.query(State).filter(State.name == sys.argv[4])
        match = state.order_by(State.id).first()
        print("Not found" if match is None else match.id)
