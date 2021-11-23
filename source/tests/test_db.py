"""
===============================================================================================
This runs tests for model.py
===============================================================================================
"""
from sys import path
path.append('..')
from unittest import TestCase
from source.model import db, Client, Room, Banlist

ROLE = 2
ROOM_NAME = "tester"
TEST_IP = "127.0.0.1"
TEST_KEY = "MyRoomTester"
CLIENT_NAME = "test_client"


class DBTestCase(TestCase):
    room = Room(key=TEST_KEY,
                host="123.456.789.010",
                name=ROOM_NAME,
                log="This is a test log.",
                mute=0,
                file=None)
    client = Client(ip=TEST_IP,
                    name="test_client",
                    role=ROLE,
                    color="000000",
                    in_room=TEST_KEY)
    banlist = Banlist(room=TEST_KEY,
                      client=TEST_IP)
    
    def test_room(self):
        """
        Test the Room table
        """
        self.assertTrue(self.room.__repr__() == '{}, {}'.format(ROOM_NAME, TEST_KEY))

    def test_client(self):
        """
        Test the User table
        """
        self.assertTrue(self.client.__repr__() == 'Client: {}:{}, Role: {}'.format(CLIENT_NAME, TEST_IP, ROLE))

    def test_banlist(self):
        """
        Test the Banlist table
        """
        self.assertTrue(self.banlist.__repr__() == 'Room: {}, IP{}'.format(TEST_KEY,TEST_IP))

if '__name__' == '__main__':
    unittest.main()
