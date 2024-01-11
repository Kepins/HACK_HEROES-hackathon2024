from functools import cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models import Base


def session():
    engine = create_engine('sqlite:///db.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

db = session()
