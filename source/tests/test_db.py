from unittest import TestCase

from source.db import fetch_games


class DBTestCase(TestCase):
    def test_fetch_games(self):
        games = fetch_games()
        self.assertTrue(isinstance(games, dict))
        self.assertTrue(len(games) > 1)
