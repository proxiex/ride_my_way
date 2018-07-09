from sqlalchemy import (Column, String, Integer, ForeignKey, Time)
from sqlalchemy.orm import relationship
from utils.database import Base
from utils.utility import Utility
from datetime import datetime


class Ride(Base, Utility):
    __tablename__ = 'rides'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    destination = Column(String, nullable=False)
    pick_up_location = Column(String, nullable=False)
    time = Column(Time, nullable=False, default=datetime.utcnow())
    number_of_seats = Column(String, nullable=False)
    role = Column(String, nullable=False)

    rides = relationship(
        'Request', backref='rides', lazy=True, cascade='all, delete-orphan')
