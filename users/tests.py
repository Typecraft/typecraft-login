# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class LoginTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User(
            username='myusername'
        )
        user.set_password('password')
        user.save()

    def test_login(self):
        response = self.client.post('/login', {
            'username': 'myusername',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.cookies.get('sessionid', ''))
        self.assertDictContainsSubset({
            'username': 'myusername',
        }, response.data)

    def test_login_with_prod_should_set_domain_name(self):
        with self.settings(SESSION_COOKIE_DOMAIN=".typecraft.org"):
            response = self.client.post('/login', {
                'username': 'myusername',
                'password': 'password'
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual('.typecraft.org', response.cookies.get('sessionid').get('domain'))

