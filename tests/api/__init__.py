# -*- coding: utf-8 -*-
"""
    tests.api
    ~~~~~~~~~

    api tests package
"""

from myapp.api import create_app

from .. import MyAppAppTestCase, settings


class MyAppApiTestCase(MyAppAppTestCase):

    def _create_app(self):
        return create_app(settings, register_security_blueprint=True)

    def setUp(self):
        super(MyAppApiTestCase, self).setUp()
        self._login()
