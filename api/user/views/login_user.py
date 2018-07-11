from flask import request
from api.user.model import User
from api.user.helpers import (
    key_missing_in_body,
    strip_clean, is_valid, response_msg,
    is_valid_email
    )


class LoginAPI:
    """
    Handles everything that has to do with users
    """

    def login(self):
        return response_msg(
           'suscess',
           'Login suscessful',
           200
           )
