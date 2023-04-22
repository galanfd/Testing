from src.clock_display import ClockDisplay
import unittest

class TestClockDisplay(unittest.TestCase):
    def test_increment(self):
        clock_display = ClockDisplay([23, 60])
        clock_display.increment()
        self.assertEqual(clock_display.str(), "00:01")

    def test_increment_2(self):
        clock_display = ClockDisplay([23, 60])
        clock_display.increment()
        clock_display.increment()
        self.assertEqual(clock_display.str(), "00:02")

    def test_clone(self):
        clock_display = ClockDisplay([23, 60])
        clock_display.increment()
        clock_display.increment()
        clone = clock_display.clone()
        self.assertEqual(clone.str(), "00:02")
    
    def test_clone_increment(self):
        clock_display = ClockDisplay([23, 60])
        clock_display.increment()
        clock_display.increment()
        clone = clock_display.clone()
        clone.increment()
        self.assertEqual(clone.str(), "00:03")
        self.assertEqual(clock_display.str(), "00:02")

    def test_invariant(self):
        clock_display = ClockDisplay([23, 60])
        self.assertTrue(clock_display.invariant(), True)

    def test_invariant_2(self):
        clock_display = ClockDisplay([23, 60])
        clock_display.increment()
        self.assertTrue(clock_display.invariant(), False)
