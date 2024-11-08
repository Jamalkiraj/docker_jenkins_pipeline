# tests/test_main.py
import unittest
from app.main import add, subtract

class TestMathOperations(unittest.TestCase):
    """Unit tests for add and subtract functions."""

    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(3, 4), 7)  # 3 + 4 should equal 7
        self.assertEqual(add(-1, 1), 0)  # -1 + 1 should equal 0
        self.assertEqual(add(0, 0), 0)   # 0 + 0 should equal 0

    def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(subtract(10, 3), 7)  # 10 - 3 should equal 7
        self.assertEqual(subtract(5, 5), 0)   # 5 - 5 should equal 0
        self.assertEqual(subtract(0, 1), -1)  # 0 - 1 should equal -1

if __name__ == '__main__':
    unittest.main()  # Run all tests when this script is executed
