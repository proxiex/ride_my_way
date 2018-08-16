from app import bcrypt


# removes white spaces.
def strip_clean(string):
    return string.strip()


def hash_pass(password):
    return bcrypt.generate_password_hash(password, 10).decode('utf-8')


def veriffy_hashed_pw(hashed_pw, password):
    return bcrypt.check_password_hash(hashed_pw, password)
