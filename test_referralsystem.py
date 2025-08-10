# test_referralsystem.py
"""
Tests for ReferralSystem module.
"""

import unittest
from referralsystem import ReferralSystem

class TestReferralSystem(unittest.TestCase):
    """Test cases for ReferralSystem class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ReferralSystem()
        self.assertIsInstance(instance, ReferralSystem)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ReferralSystem()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
