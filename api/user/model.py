from sqlalchemy import (Column, String, Integer, )
from sqlalchemy.orm import relationship
from utils.database import Base
from utils.utility import Utility
from api.ride.model import Ride  # noqa: F401
from api.request.model import Request  # noqa: F401
# from api.friend.model import Friend  # noqa: F401


class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    rides = relationship(
        'Ride', backref='users', lazy=True, cascade='all, delete-orphan')
    requests = relationship(
        'Request', backref='users', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return "<User: {}>". format(
            self.id,
            self.first_name,
            self.last_name,
            self.username,
            self.email
        )
