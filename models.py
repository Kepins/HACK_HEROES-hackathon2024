from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Tour(Base):
    __tablename__ = 'tour'

    id = Column(Integer, primary_key=True)


class Path(Base):
    __tablename__ = 'path'

    id = Column(Integer, primary_key=True)
    pick_up = Column(String)
    count = Column(Integer)
    path_to_png = Column(String)

    tour_id = Column(Integer, ForeignKey('path.id'))
    tour = relationship('Tour', back_populates='paths')
