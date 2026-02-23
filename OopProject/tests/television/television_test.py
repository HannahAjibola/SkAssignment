import unittest
from typing import assert_never

from src.television.tele_vision import Tv


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tv = Tv()

    def test_that_tv_is_on(self):
        self.tv.is_on()
        self.assertTrue(self.tv.is_on)

    def test_that_tv_is_off(self):
        self.tv.is_on()
        self.tv.is_off()
        self.assertFalse(self.tv.is_on())

    def test_that_tv_increase_volume_works(self):
        self.tv.increase_volume(60)
        self.assertEqual(self.tv.increase_volume(), 60)


if __name__ == '__main__':
    unittest.main()
