from app import bcrypt


# removes white spaces.
def strip_clean(string):
    return string.strip()


def hash_pass(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')
