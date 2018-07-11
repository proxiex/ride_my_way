
empyt_user = {}

new_user = {
    "first_name": "Biskyet",
    "last_name": "Nanpit",
    "username": "Bis",
    "email": "loveme@me.com",
    "password": "password"
}

empty_user_first_name = {
    "first_name": "",
    "last_name": "Nanpit",
    "username": "Bis",
    "email": "loveme@me.com",
    "password": "password"
}

no_first_name = {
    "last_name": "Nanpit",
    "username": "Bis",
    "email": "loveme@me.com",
    "password": "password"
}

user_first_name_with_special_chars = {
    "first_name": "Biskyet@",
    "last_name": "Nanpit",
    "username": "Bis",
    "email": "loveme@me.com",
    "password": "password"
}

user_last_name_with_special_chars = {
    "first_name": "Biskyet",
    "last_name": "Nanpit$",
    "username": "Bis",
    "email": "loveme@me.com",
    "password": "password"
}

user_username_with_special_chars = {
    "first_name": "Biskyet",
    "last_name": "Nanpit",
    "username": "Bis%",
    "email": "loveme@me.com",
    "password": "password"
}

new_user_exist_response = {
    "message": "This email \"loveme@me.com\" is already associated with an account",  # noqa: E501
    "status": "fail"
}
