#!/bin/env python
from flask import Flask
from source.socket import socketio

def create_app(debug=True):
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'randomkey'

    from source.route import main as main_blueprint
    app.register_blueprint(main_blueprint)
    socketio.init_app(app)
    import source.events
    return app


if __name__ == '__main__':
    app = create_app()

    socketio.run(app)
