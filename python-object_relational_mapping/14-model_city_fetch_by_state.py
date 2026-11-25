#!/usr/bin/python3
"""List city models with their states in city ID order."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session

from model_city import City
from model_state import Base, State


if __name__ == "__main__":
    url = URL.create("mysql+mysqldb", username=sys.argv[1],
                     password=sys.argv[2], host="localhost", port=3306,
                     database=sys.argv[3])
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        cities = session.query(City, State.name).join(State)
        for city, state_name in cities.order_by(City.id):
            print(f"{state_name}: ({city.id}) {city.name}")
