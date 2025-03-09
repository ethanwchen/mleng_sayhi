"""Unit tests for the main application."""

import unittest
from mleng_sayhi.app import add_numbers

class TestApp(unittest.TestCase):
    """Test cases for the add_numbers function."""

    def test_add_numbers(self):
        """Test if add_numbers correctly adds two numbers."""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_add_numbers_negative(self):
        """Test if add_numbers handles negative numbers correctly."""
        self.assertEqual(add_numbers(-5, -5), -10)
        self.assertEqual(add_numbers(-3, 7), 4)

if __name__ == "__main__":
    unittest.main()
