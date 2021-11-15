"""
===============================================================================================
This runs tests for model.py
===============================================================================================
"""
from sys import path
path.append('..')
from unittest import TestCase
from source.model import db, User, Room, Banlist

ROLE = 2
ROOM_NAME = "tester"
TEST_IP = "127.0.0.1"
TEST_KEY = "MyRoomTester"
TEST_ROOM = Room(key=TEST_KEY,
                 host="123.456.789.010",
                 name=ROOM_NAME,
                 log="This is a test log.",
                 mute=0,
                 file=None)
TEST_USER = User(ip=TEST_IP,
                 name="test_user",
                 role=ROLE,
                 color="000000",
                 in_room=TEST_KEY)
USER_NAME = "test_user"


class DBTestCase(TestCase):
    def test_room(self):
        """
        Test the Room table
        """
        test_room = TEST_ROOM
        self.assertTrue(test_room.__repr__() == '{}, {}'.format(ROOM_NAME, TEST_KEY))

    def test_user(self):
        """
        Test the User table
        """
        test_room = TEST_ROOM
        test_user = TEST_USER
        self.assertTrue(test_user.__repr__() == 'User: {}:{}, Role: {}'.format(USER_NAME, TEST_IP, ROLE))

    def test_banlist(self):
        """
        Test the Banlist table
        """
        test_room = TEST_ROOM
        test_user = TEST_USER
        test_ban = Banlist(room=TEST_KEY,
                           ip=TEST_IP)
        self.assertTrue(test_ban.__repr__() == 'Room: {}, IP{}'.format(TEST_KEY,TEST_IP))

if '__name__' == '__main__':
    unittest.main()
