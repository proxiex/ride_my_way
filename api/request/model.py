from sqlalchemy import (Column, Integer, Boolean, ForeignKey)
from utils.database import Base
from utils.utility import Utility


class Request(Base, Utility):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    ride_id = Column(Integer, ForeignKey('rides.id'))
    status = Column(Boolean, nullable=False)
