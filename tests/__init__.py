# -*- coding: utf-8 -*-
"""
    tests
    ~~~~~

    tests package
"""

from unittest import TestCase

from myapp.core import db

from .factories import UserFactory
from .utils import FlaskTestCaseMixin


class MyAppTestCase(TestCase):
    pass


class MyAppAppTestCase(FlaskTestCaseMixin, MyAppTestCase):

    def _create_app(self):
        raise NotImplementedError

    def _create_fixtures(self):
        self.user = UserFactory()

    def setUp(self):
        super(MyAppAppTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self._create_fixtures()
        self._create_csrf_token()

    def tearDown(self):
        super(MyAppAppTestCase, self).tearDown()
        db.drop_all()
        self.app_context.pop()

    def _login(self, email=None, password=None):
        email = email or self.user.email
        password = password or 'password'
        return self.post('/login', data={'email': email, 'password': password},
                         follow_redirects=False)
