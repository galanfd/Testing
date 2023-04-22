from src.display_number import NumberDisplay
import unittest

class TestNumberDisplay(unittest.TestCase):

    def test_invariant(self):
        number_display = NumberDisplay(0, 60)
        self.assertTrue(number_display.invariant())

    def test_invariant_2(self):
        number_display = NumberDisplay(61, 60)
        self.assertFalse(number_display.invariant())

    def test_invariant_3(self):
        number_display = NumberDisplay(60, 60)
        self.assertFalse(number_display.invariant())

    def test_increase(self):
        number_display = NumberDisplay(0, 60)
        number_display.increase()
        self.assertEqual(number_display.value, 1)