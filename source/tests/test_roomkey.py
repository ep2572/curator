"""
==============================
This runs tests for roomkey.py
==============================
"""

from unittest import TestCase
from source.roomkey import get_roomkey

class TestRoomkey(TestCase):
    key = get_roomkey()
    
    def test_roomkey_alnum(self):
        """
        Test that roomkey gives alphanumeric
        """
        self.assertTrue(self.key.isalnum())

    def test_roomkey_len(self):
        """
        Test that roomkey has a length of 12
        """
        self.assertTrue(len(self.key) == 12)
