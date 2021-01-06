from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

# Custom decorators that check user permissions
# Mukautetut sisustajat, jotka tarkistavat käyttäjien oikeudet
# decorators are built with the help of the functools package from the Python standard library, and return an error code 403,#
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMIN)(f)