#!/usr/bin/python3
"""Fetch cities by state"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    rows = session.query(City.id, City.name, State.name).join(
        State).order_by(City.id).all()
    for cid, cname, sname in rows:
        print("{}: ({}) {}".format(sname, cid, cname))
    session.commit()
    session.close()
