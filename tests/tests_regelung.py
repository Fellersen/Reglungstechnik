import unittest

from src.regelung import addieren


class TestRegelung(unittest.TestCase):
    def test_addieren(self):
        self.assertEqual(addieren(a=1, b=1), 2)
