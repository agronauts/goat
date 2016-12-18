from django.test import TestCase

class SmokeTest(TestCase):

    def test_horrible_math(self):
        self.assertEqual(1+1, 21)
