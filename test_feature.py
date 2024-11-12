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


# Custom TestResult to suppress traceback for failures
class CustomTestResult(unittest.TextTestResult):
    def addFailure(self, test, err):
        # Suppress traceback, and only report the failure in a custom format
        print(f"FAIL: {test}")
        # Add a dummy error message (so unittest doesn't throw formatting errors)
        self.failures.append((test, 'FAILURE'))

    def addError(self, test, err):
        # Suppress traceback for errors as well
        print(f"FAIL: {test}")
        # Add a dummy error message (so unittest doesn't throw formatting errors)
        self.errors.append((test, 'ERROR'))


# Custom TextTestRunner that uses our CustomTestResult
class CustomTextTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)


if __name__ == '__main__':
    # Use the custom test runner to suppress tracebacks
    runner = CustomTextTestRunner(verbosity=2)
    result = runner.run(unittest.TestLoader().loadTestsFromTestCase(TestCalculator))

    # Custom output formatting
    print("\nTest Results Summary:")

    # Failures: Only count actual failed tests (not skipped)
    failure_count = len(result.failures) + len(result.errors)

    # Successes: Total tests run minus failures
    success_count = result.testsRun - failure_count

    print(f"Total Successes: {success_count}")
    print(f"Total Failures: {failure_count}")

    # Final summary
    if result.wasSuccessful():
        print("\nAll tests passed!")
    else:
        print(f"\nSome tests failed. Total failures: {failure_count}")
