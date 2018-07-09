from flask import make_response, jsonify


# method to check whether key is missing in request
def key_missing_in_body(data):
    # check if key is present in data
    keys = ('first_name', 'last_name', 'email', 'username', 'password')
    for key in keys:
        if key not in data:
            return True


def validate_empty_fields(data):
    """
    Function to validate empty fields when
    saving an object
    :params kwargs
    """
    for field in data:
        if not data.get(field):
            return True


# string string to remove white spaces
def strip_clean(string):
    return string.strip()


def is_valid(name_string):
    special_character = "~!@#$%^&*()_={}|\[]<>?/,;:"
    return any(char in special_character for char in name_string)


def response_msg(status, msg, status_code, help_msg=None, data=None):
    """ Response Message
    :param:
        :status: string
        :msg: string
        :status_code: integer
        :help_msg: string | deffault: None
        :data: dict | deffault: None
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

    return make_response(jsonify(response)), status_code
