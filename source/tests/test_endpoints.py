
"""
This runs tests for endpoints.py.
"""

from unittest import TestCase
from flask_restx import Resource
import json
from source.endpoints import HelloWorld, HELLO, AVAILABLE, Endpoints, HOME, CHATROOM, Home, Chatroom
from source.endpoints import HowTo, DATA_DIR, HOW_TO_JSON


class TestEndpoints(TestCase):
    def test_home(self):
        """
        Test "home" endpoint.
        """
        home_ep = Home(Resource)
        ret = home_ep.get()
        self.assertIn(HOME, ret)
        
    def test_chatroom(self):
        """
        Test "chatroom" endpoint.
        """
        chat_ep = Chatroom(Resource)
        ret = chat_ep.put(12345)
        self.assertIn(CHATROOM, ret)
        
    def test_hello(self):
        """
        Test "hello" endpoint.
        """
        hello_ep = HelloWorld(Resource)
        ret = hello_ep.get()
        self.assertIn(HELLO, ret)

    def test_endpoints(self):
        """
        Test "endpoints" endpoint.
        """
        epts = Endpoints(Resource)
        ret = epts.get()
        self.assertIn(AVAILABLE, ret)

    def test_how_to(self):
        """
        Test "howto" endpoint.
        """
        how2 = HowTo(Resource)
        ret = how2.get()
