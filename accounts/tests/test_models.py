from django.contrib import auth
from django.test import TestCase

from accounts.models import User, Token


class UserModelTest(TestCase):

    def test_user_is_valid_with_email_only(self):
        new_user = User(email='ichigo@heaven.sky')
        new_user.full_clean()

    def test_email_is_primary_key(self):
        user = User()
        self.assertFalse(hasattr(user, 'id'))

    def test_email_in_repr(self):
        email = 'ghandi@peace@ind'
        user = User(email)
        self.assertTrue(email in repr(user))

    def test_no_problem_with_auth_login(self):
        user = User.objects.create(email='jerry.rawlings@reluctance.gh')
        user.backend = ''
        request = self.client.request().wsgi_request
        auth.login(request, user) # Should not raise


class TokenModelTest(TestCase):


    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email='a@b.com')
        token2 = Token.objects.create(email='a@b.com')
        self.assertNotEqual(token1.uid, token2.uid)

