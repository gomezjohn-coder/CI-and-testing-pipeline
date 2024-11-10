import unittest

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)  # Pass

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)  # Pass

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)  # Pass

    def test_add_fail(self):
        self.assertEqual(add(10, 5), 20)  # Fail intentionally

    def test_subtract_fail(self):
        self.assertEqual(subtract(10, 5), 10)  # Fail intentionally

if __name__ == '__main__':
    unittest.main(verbosity=2)
