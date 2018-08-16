from flask import make_response, jsonify
import re


# method to check whether key is missing in request
def key_missing_in_body(data):
    # check if key is present in data
    keys = ('first_name', 'last_name', 'email', 'username', 'password')
    for key in keys:
        if key not in data:
            return True


# string string to remove white spaces
def strip_clean(string):
    return string.strip()


# method to check whether email is valid
def is_valid_email(email):
    match = re.search(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",
        email
    )
    if match:
        return True
    else:
        return False


def is_valid(name_string):
    special_character = "~!@#$%^&*()_={}|\[]<>?/,;:"
    return any(char in special_character for char in name_string)


def response_msg(status, msg, status_code, help_msg=None, data=None, token=None):  # noqa: E501
    """ Response Message
    :param:
        :status: string
        :msg: string
        :status_code: integer
        :help_msg: string | default: None
        :data: dict | default: None
        :token: token | default: None
    :return:
        Json object
    """

    response = {
        'status': status,
        'message': msg
    }

    if help_msg:
        response['helpMessage'] = help_msg

    if data:
        response['data'] = data

    if token:
        response['token'] = token

    return make_response(jsonify(response)), status_code
