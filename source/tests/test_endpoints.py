
"""
This runs tests for endpoints.py.
"""

from unittest import TestCase
from flask_restx import Resource

from source.endpoints import HelloWorld, HELLO, AVAILABLE, Endpoints, Home, Chatroom
from source.endpoints import Games


class TestEndpoints(TestCase):
    def test_home(self):
        """
        Test our "home" endpoint.
        """
        home_ep = Home(Resource)
        ret = home_ep.get()
        self.assertIn(ret)
        
    def test_chatroom(self):
        """
        Test our "chatroom" endpoint.
        """
        chat_ep = Chatroom(Resource)
        ret = chat_ep.get()
        self.assertIn(ret)
        
    def test_hello(self):
        """
        Test our "hello" endpoint.
        """
        hello_ep = HelloWorld(Resource)
        ret = hello_ep.get()
        self.assertIn(HELLO, ret)

    def test_endpoints(self):
        """
        Test our "endpoints" endpoint.
        """
        epts = Endpoints(Resource)
        ret = epts.get()
        self.assertIn(AVAILABLE, ret)

    def test_games_list(self):
        """
        Test our "games/list" endpoint.
        """
        games = Games(Resource)
        ret = games.get()
        self.assertIsInstance(ret, dict)
        # we expect more than one game type!
        self.assertGreater(len(ret), 1)
