
from src.clock_factory import ClockFactory
import unittest

class TestClockFactory(unittest.TestCase):
    def test_creat_hhmmss(self):
        clock_factory = ClockFactory()
        clock = clock_factory.create("hh:mm:ss")
        self.assertEqual(clock.str(), "00:00:00")

    def test_creat_hhmm(self):
        clock_factory = ClockFactory()
        clock_display = clock_factory.create("hh:mm")
        self.assertEqual(clock_display.str(), "00:00")
    
    def test_create_hhmmssmmmm(self):
        clock_factory = ClockFactory()
        clock_display = clock_factory.create("hh:mm:ss:mmmm")
        self.assertEqual(clock_display.str(), "00:00:00:00")

# if __name__ == '__main__':
#     unittest.main()