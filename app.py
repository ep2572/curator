#!/bin/env python
from flask import Flask
#import psycopg2
from source.socket import socketio
import source.roomkey
from source.moodels import db

app = Flask(__name__)
app.debug = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 *1000
app.config['SECRET_KEY'] = 'randomkey'

db.init_app(app)

from source.route import main as main_blueprint
app.register_blueprint(main_blueprint)
socketio.init_app(app)
import source.events

if __name__ == '__main__':
    socketio.run(app)

# Host be an issue once it's transferred to Heroku
##conn = psycopg2.connect(
##    database = "data/curator",
##    user = "curator",
##    password = "design_proj",
##    host = "127.0.0.1", 
##    port = "8080")
##cur = conn.cursor()
