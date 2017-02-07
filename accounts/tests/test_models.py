from django.test import TestCase

from accounts.models import User, Token


class UserModelTest(TestCase):

    def test_user_is_valid_with_email_only(self):
        new_user = User(email='ichigo@heaven.sky')
        new_user.full_clean()

    def test_things(self):
        pass

class TokenModelTest(TestCase):


    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email='a@b.com')
        token2 = Token.objects.create(email='a@b.com')
        self.assertNotEqual(token1.uid, token2.uid)

