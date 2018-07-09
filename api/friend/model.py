from sqlalchemy import (Column, Integer, Boolean, ForeignKey)
from sqlalchemy.orm import relationship
from utils.database import Base
from utils.utility import Utility
from api.user.model import User  # noqa: F401


class Friend(Base, Utility):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    request_id = Column(Integer, ForeignKey('users.id'))
    status = Column(Boolean, nullable=False)

    users = relationship(
        'User',
        foreign_keys='user_id',
        backref='users', lazy=True, cascade='all, delete-orphan')
    request = relationship(
        'User',
        foreign_keys='request_id',
        backref='users', lazy=True, cascade='all, delete-orphan')
