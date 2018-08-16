from flask import request
from sqlalchemy import or_
from api.user.model import User
from api.user.helpers import (
    strip_clean, response_msg
    )
import datetime
import jwt


class LoginAPI:
    """
    Handles everything that has to do with users
    """

    def login(self):
        try:
            response = response_msg(
                'fail',
                'Please pass in data',
                400,
                'identifier [email or username]]: str: str, password: str',
                )
            if not request.get_json(force=True):
                return response
        except Exception as e:
            return response
        data = request.get_json(force=True)
        if data:
            from helpers import veriffy_hashed_pw
            from app import app

            keys = ('identifier', 'password')
            for key in keys:
                if key not in data:
                    return response_msg(
                        'fail',
                        'All fields are required',
                        400,
                        'identifier [email or username]: str, password: str'
                        )

            identifier = data['identifier']
            password = data['password']

            if strip_clean(identifier) == '' or strip_clean(password) == '':
                return response_msg(
                    'fail',
                    'All flieds must be filled',
                    400
                )
            login_res = response_msg(
                'fail',
                'Invalid login credentials',
                400
                )
            # query the database for user authentication
            user = User.query.filter(or_(
                User.email == data['identifier'],
                User.username == data['identifier'])
                ).first()

            if user:
                if veriffy_hashed_pw(user.password, password):
                    payload = {
                            'id': user.id,
                            'first_name': user.first_name,
                            'last_name': user.last_name,
                            'email': user.email,
                            'username': user.username,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),  # noqa: E501
                        }

                    token = jwt.encode(payload, app.config.get('SECRET_KEY')).decode('utf-8')   # noqa: E501
                    return response_msg(
                        'sucess',
                        'Login was succesful',
                        200,
                        None,
                        None,
                        token
                    )
                else:
                    return login_res
            else:
                return login_res
