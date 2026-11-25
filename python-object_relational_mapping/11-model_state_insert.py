#!/usr/bin/python3
"""Insert Louisiana and print its generated ID."""

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
        state = State(name="Louisiana")
        session.add(state)
        session.flush()
        identifier = state.id
        session.commit()
        print(identifier)
