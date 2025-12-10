# test_ordernotifier.py
"""
Tests for OrderNotifier module.
"""

import unittest
from ordernotifier import OrderNotifier

class TestOrderNotifier(unittest.TestCase):
    """Test cases for OrderNotifier class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OrderNotifier()
        self.assertIsInstance(instance, OrderNotifier)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OrderNotifier()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
