# -*- coding: utf-8 -*-
"""
    myapp.users
    ~~~~~~~~~~~~~~

    myapp users package
"""

from ..core import Service
from .models import User


class UsersService(Service):
    __model__ = User
