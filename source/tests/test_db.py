from unittest import TestCase

from app import db, User, Room, Banlist
import source.roomkey

class DBTestCase(TestCase):
    def test_user(self):
        test_user = User(ip="127.0.0.1",
                         name="test_user",
                         role=1,
                         color="000000",
                         in_room="")
        self.assertTrue(test_user == "User: test_user:127.0.0.1, Role: 2")

    def test_room(self):
        test_room = Room(key="MyRoomTester",
                         host="123.456.789.010",
                         name="tester",
                         log="This is a test log.",
                         mute=0,
                         file=None)
        self.assertTrue(test_room == "tester, MyRoomTester")
