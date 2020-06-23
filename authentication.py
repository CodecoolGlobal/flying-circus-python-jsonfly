from functools import wraps

from flask import session, Response

import data


def verify_password(email, password):
    if email not in data.users:
        return 'Valami baj van', 400

    if data.users[email] == password:
        session['username'] = email
        return 'Logged in', 200
    else:
        return 'Wrong password', 400


def get_actual_user_data():
    return session['username']


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return Response('Unauthorized!', 401)
        return f(*args, **kwargs)
    return wrapper