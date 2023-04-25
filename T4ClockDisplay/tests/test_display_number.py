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

    def test_increase_limitreach(self):
        number_display = NumberDisplay(59, 60)
        ret = number_display.increase()
        self.assertEqual(ret, True)

    def test_mutant_iftrue(self):
        number_display = NumberDisplay(10, 60)
        self.assertEqual(number_display.str(), "10")

    def test_mutant_iftrue2(self):
        number_display = NumberDisplay(9, 60)
        self.assertEqual(number_display.str(), "09")

    def test_mutant_iftrue3(self):
        number_display = NumberDisplay(11, 60)
        self.assertEqual(number_display.str(), "11")

    def test_reset(self):
        number_display = NumberDisplay(59, 60)
        number_display.reset()
        self.assertEqual(number_display.value, 0)

    def test_reset_valor0(self):
        number_display = NumberDisplay(5, 10)
        self.assertNotEqual(number_display.value, 0)
        number_display.reset()
        self.assertEqual(number_display.value, 0)

    def test_returnNone(self):
        number_display = NumberDisplay(10, 20)
        self.assertIsNone(number_display.__init__(10, 20))
