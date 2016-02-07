# -*- coding: utf-8 -*-
"""
    myapp.api.users
    ~~~~~~~~~~~~~~~~~~

    User endpoints
"""

from flask import Blueprint
from flask_login import current_user

from ..services import users
from . import route

bp = Blueprint('users', __name__, url_prefix='/users')


@route(bp, '/')
def whoami():
    """Returns the user instance of the currently authenticated user."""
    # flask_security.core.AnonymousUser is not JSON serializable (and we haven't implemented way to serialize)
    # so for now, we simply skip the object and return  "Anonymous" so client gets { "data": "Anonymous" }
    if current_user.is_anonymous:
        return "Anonymous"
    else:
        return current_user._get_current_object()


@route(bp, '/<user_id>')
def show(user_id):
    """Returns a user instance."""
    return users.get_or_404(user_id)
