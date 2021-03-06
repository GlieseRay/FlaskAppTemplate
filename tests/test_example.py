# -*- encoding: utf-8 -*-

import os
import unittest
from example import AppBuilder


class TestExample(unittest.TestCase):
    def setUp(self):

        os.environ['EXAMPLE_APP_ENV'] = 'dev'

        app = AppBuilder().build()
        self.client = app.test_client()

    def test_app(self):
        resp = self.client.get('/')
        self.assertEqual('Hello World!', resp.data)

