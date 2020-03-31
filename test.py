# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from raj_algebra import Algebra

class TestAlgebra(unittest.TestCase):
    def setUp(self):
        self.a = Algebra()

    def test_addition(self):
        self.assertEqual(self.a.addition(1,3), 4)

    def test_subtraction(self):
        self.assertEqual(self.a.subtraction(3,1), 2)

    def test_multiplication(self):
        self.assertEqual(self.a.multiplication(2,3), 6)

    def test_division(self):
        self.assertEqual(self.a.division(6,3), 2)