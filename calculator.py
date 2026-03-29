import unittest

# --- CORE FUNCTIONS ---
def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

def square(number):
    return number * number

def cube(number):
    return number * number * number

def is_positive(number):
    return number > 0

# --- UNIT TESTS ---
class TestNumberAnalyzer(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual(is_even(4), True)
        self.assertEqual(is_even(7), False)

    def test_is_odd(self):
        self.assertEqual(is_odd(5), True)
        self.assertEqual(is_odd(8), False)

    def test_is_square(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(2), 4)

    def test_is_cube(self):
        self.assertEqual(cube(3), 27)
        self.assertEqual(cube(2), 8)

    def test_is_positive(self):
        self.assertEqual(is_positive(5), True)
        self.assertEqual(is_positive(-3), False)

if __name__ == '__main__':
    unittest.main()