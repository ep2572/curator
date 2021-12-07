"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Resource, Api
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)
api = Api(app)

HOME = 'Home'
CHATROOM = 'Chatroom'
HELLO = 'hello'
AVAILABLE = 'Available endpoints:'
DATA_DIR = '../data'
HOW_TO_JSON = DATA_DIR + '/' + 'how_to.json'


def get_how_to():
    print("Going to open {HOW_TO_JSON}")
    try:
        with open(HOW_TO_JSON) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print('Failed to find {}'.format(HOW_TO_JSON))
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


@api.route('/how_to')
class HowTo(Resource):
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
        how_to = get_how_to()
        if how_to is None:
            raise (NotFound("How To not found."))
        return how_to
