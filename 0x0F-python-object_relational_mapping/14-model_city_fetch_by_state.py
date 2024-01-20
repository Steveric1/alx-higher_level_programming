#!/usr/bin/python3
"""Write a Python file similar to model_state.py named model_city.py
that contains the class definition of a City."""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    city_inst = (session.query(State.name, City.id, City.name)
                 .filter(State.id == City.state_id).all())

    for inst in city_inst:
        print(inst[0] + ": (" + str(inst[1]) + ") " + inst[2])
    session.close()
