from flask import request
from api.user.model import User
from api.user.helpers import (
    key_missing_in_body,
    strip_clean, is_valid, response_msg,
    is_valid_email
    )


class RegisterAPI:
    """
    Handles everything that has to do with users
    """

    def create(self):
        # validate data - if data is passed or not

        try:
            response = response_msg(
                    'fail',
                    'Please pass in data',
                    400,
                    'first_name: str, last_name: str, username: str, email: str, password: str',  # noqa: E501
                    )

            if not request.get_json(force=True):
                return response
        except Exception as e:
            return response

        data = request.get_json(force=True)
        if data:
            from helpers import hash_pass

            # check if any field is missing
            if key_missing_in_body(data):
                return response_msg(
                    'fail',
                    'All fields are requried',
                    400,
                    'first_name: str, last_name: str, username: str, email: str, password: str',  # noqa: E501
                    )  # noqa: E501

            first_name = data['first_name']
            last_name = data['last_name']
            username = data['username']
            email = data['email']
            password = data['password']
            data['password'] = hash_pass(password)

            # check if any field is emtpy
            if strip_clean(first_name) == '' or\
               strip_clean(last_name) == '' or\
               strip_clean(username) == '' or\
               strip_clean(email) == '' or\
               strip_clean(password) == '':
                return response_msg(
                    'fail',
                    'All fields must be filled',
                    400
                )

            if is_valid(first_name):
                return response_msg(
                    'fail',
                    'first_name contains special characters',
                    400
                )

            if is_valid(last_name):
                return response_msg(
                    'fail',
                    'last_name contains special characters',
                    400)

            if is_valid(username):
                return response_msg(
                    'fail',
                    'username contains special characters',
                    400
                )

            if not is_valid_email(email):
                return response_msg(
                    'fail',
                    'Invalid Email address',
                    400
                )

            if len(password) < 6:
                return response_msg(
                    'fail',
                    'Password is too short, it should be greater than 6',
                    400
                )

        user = User.query.filter_by(email=data['email']).first()

        if not user:
            try:
                new_user = User(**data)
                new_user.save()

                new_data = {}
                new_data['id'] = new_user.id
                new_data['frist_name'] = new_user.first_name
                new_data['last_name'] = new_user.last_name
                new_data['username'] = new_user.username
                new_data['email'] = new_user.email

                return response_msg(
                    'success',
                    'Successfully registered',
                    201,
                    None,
                    new_data
                    )
            except Exception as e:
                return response_msg(
                    'fail',
                    'Some error occured, please try again!',
                    500
                )
        else:
            return response_msg(
                'fail',
                'This email "'+email+'" is already associated with an account',  # noqa: E501
                409
            )
