from unittest import TestCase

from source.db import fetch_games
import source.roomkey

class DBTestCase(TestCase):
    def test_fetch_games(self):
        games = fetch_games()
        self.assertTrue(isinstance(games, dict))
        self.assertTrue(len(games) > 1)

    def test_gen_roomkey(self):
        roomkey1 = get_roomkey()
        roomkey2 = get_roomkey()
        self.assertTrue(roomkey1.isalnum())
        self.assertTrue(roomkey2.isalnum())
