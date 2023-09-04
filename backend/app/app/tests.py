"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """Test adding two numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)