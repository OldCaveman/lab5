import unittest
from gdd import calculate


class TestGDD(unittest.TestCase):

    def test_gdd(self):
        self.assertEquals(-32.5, calculate(high=23, low=12, base=50))
        self.assertEquals(-38.5, calculate(13, 10, base=50))
        self.assertEquals(-38.5, calculate(13, 10))
        self.assertEquals(-38.5, calculate(13, 10))
        self.assertEquals(-0.5, calculate(13, 10, 12))


if __name__ == '__main__':
    unittest.main()
