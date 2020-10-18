import unittest
from main import factorial


class TestFactorial(unittest.TestCase):
    def setUp(self):
        pass

    # Returns True if the factorial is correct.
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
