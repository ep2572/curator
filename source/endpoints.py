"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

import json
from flask import Flask
from flask_restx import Resource, Api, fields
from werkzeug.exceptions import NotFound

from source.db import fetch_games

app = Flask(__name__)
api = Api(app)

HOME = 'Home'
CHATROOM = 'Chatroom'
HELLO = 'hello'
AVAILABLE = 'Available endpoints:'
MAIN_MENU = "Main Menu"
MAIN_MENU_ROUTE = '/menus/main'

DATA_DIR = '../data'
MAIN_MENU_JSON = DATA_DIR + '/' + 'main_menu.json'


def get_main_menu():
    print(f"Going to open {MAIN_MENU_JSON}")
    try:
        with open(MAIN_MENU_JSON) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None


@api.route('/<int:roomkey>')
class Chatroom(Resource):
    """
    Attempting to add a new route: Chatroom
    """
    def put(self, roomkey):
        """
        For now this will just return a line of text
        """
        return {CHATROOM: "Joined."}


@api.route('/')
class Home(Resource):
    """
    The landing page for the web app
    """
    def get(self):
        """
        Trivial check to make sure that the endpoint is working
        """
        return {HOME: 'endpoint is available'}


@api.route('/hello')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {HELLO: 'world'}


@api.route('/endpoints/list')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        epts = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {AVAILABLE: epts}


@api.route(MAIN_MENU_ROUTE)
class MainMenu(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    @api.response(200, 'Success')
    @api.response(404, 'Not Found')
    def get(self):
        """
        The `get()` method will return the main menu.
        """
        main_menu = get_main_menu()
        if main_menu is None:
            raise (NotFound("Main menu not found."))
        return main_menu


@api.route('/games/list')
class Games(Resource):
    """
    This class supports fetching a list of all games.
    """
    def get(self):
        """
        This method returns all games.
        """
        return fetch_games()


user = api.model("user", {
    "name": fields.String("User name."),
    "ip": fields.String("127.0.0.1"),
    "color": fields.String("#000000"),
    "status": fields.String("User")
})


@api.route('/games/join/<int:game_id>')
class JoinGame(Resource):
    """
    This endpoint allows a user to join an existing game.
    """
    @api.expect(user)
    def put(self, game_id):
        return "Game joined."


@api.route('/games/create')
class CreateGame(Resource):
    """
    This class allows the user to create a new game.
    We will be passing in some sort of game object as a
    parameter. Details unknown at present.
    """
    def post(self):
        """
        This method returns all games.
        """
        return "Game created."
