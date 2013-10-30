import unittest
from gdd import calculate


class TestGDD(unittest.TestCase):

    def test_gdd(self):
        self.assertEquals(0, calculate(high=23, low=12, base=50))
        self.assertEquals(20, calculate(80, 60, 50))


if __name__ == '__main__':
    unittest.main()
