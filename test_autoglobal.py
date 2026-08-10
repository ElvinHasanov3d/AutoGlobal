# test_autoglobal.py
"""
Tests for AutoGlobal module.
"""

import unittest
from autoglobal import AutoGlobal

class TestAutoGlobal(unittest.TestCase):
    """Test cases for AutoGlobal class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AutoGlobal()
        self.assertIsInstance(instance, AutoGlobal)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AutoGlobal()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
