import unittest

from src.utility import Utility


class FakeLogger:
    def __init__(self):
        self.infos = []
        self.errors = []

    def info(self, message):
        self.infos.append(message)

    def error(self, message):
        self.errors.append(message)


class TestUtilityDivision(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()
        self.utility = Utility(self.logger)

    def test_division_returns_quotient(self):
        self.assertEqual(self.utility.division(10, 2), 5.0)
        self.assertEqual(self.logger.infos, ["a = 10.0", "b = 2.0"])

    def test_division_accepts_numeric_strings(self):
        self.assertEqual(self.utility.division("9", "3"), 3.0)

    def test_division_by_zero_returns_error(self):
        result = self.utility.division(10, 0)
        self.assertEqual(result, "input is invalid - cannot divide by zero")
        self.assertEqual(self.logger.errors, ["input is invalid - cannot divide by zero"])

class TestUtilityAddition(unittest.TestCase):
     def setUp(self):
        self.logger = FakeLogger()
        self.utility = Utility(self.logger)

     def test_addition_returns_sum(self):
        self.assertEqual(self.utility.addition(2, 3), 5.0)
        self.assertEqual(self.logger.infos, ["a = 2.0", "b = 3.0"])

     def test_addition_by_zero_returns_same_value(self):
        self.assertEqual(self.utility.addition(10, 0), 10.0)

class   TestUtilityMultiplication(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()
        self.utility = Utility(self.logger)

    def test_multiplication_returns_product(self):
        self.assertEqual(self.utility.multiplication(2, 3), 6.0)
        self.assertEqual(self.logger.infos, ["a = 2.0", "b = 3.0"])

    def test_multiplication_accepts_numeric_strings(self):
        self.assertEqual(self.utility.multiplication("2", "3"), 6.0)

if __name__ == "__main__":
    unittest.main()
