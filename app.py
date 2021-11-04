#!/bin/env python
from flask import Flask
#import psycopg2
from source.socket import socketio
import source.roomkey

app = Flask(__name__)
app.debug = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 *1000
app.config['SECRET_KEY'] = 'randomkey'


# Host be an issue once it's transferred to Heroku
##conn = psycopg2.connect(
##    database = "data/curator",
##    user = "curator",
##    password = "design_proj",
##    host = "127.0.0.1", 
##    port = "8080")
##cur = conn.cursor()

"""
===============================================================================
# Models for the database
# Users(Many) to Rooms(Many)
===============================================================================
"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

KEY_SIZE = 12
IPV4_MAX_LENGTH = 15

"""
A client can be in multiple rooms at once, with different names,
colors, and roles. A new instance of the client class is given
to the client for each room the are in.
"""
class User(db.Model):
    ip = db.Column(db.String(IPV4_MAX_LENGTH), primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    # role: 0 is guest, 1 is moderator, 2 is host
    role = db.Column(db.SmallInteger, default=0)
    # Default color is Black 0x000000
    color = db.Column(db.String(6), default='000000', nullable=False)
    in_room = db.Column(db.String(KEY_SIZE), db.ForeignKey('room.key'),
                        primary_key=True)
    def __repr__(self):
        return 'User: {}:{}, Role: {}'.format(self.name, self.ip, self.role)
                     
"""
A rooms only exists so long as 1 User is still present. Each room
will maintain the chat log, 
"""
class Room(db.Model):
    key = db.Column(db.String(KEY_SIZE), primary_key=True)
    host = db.Column(db.String(IPV4_MAX_LENGTH), nullable=False)
    name = db.Column(db.String(512), default='curator room '+key)
    log = db.Column(db.Text, default='')
    mute = db.Column(db.Boolean, default=False)
    file = db.Column(db.LargeBinary)

    def __repr__(self):
        return "''{}, {}".format(self.name, self.key)

"""
Each instance of the Banlist has only one room and one user IP
"""
class Banlist(db.Model):
    room = db.Column(db.String(KEY_SIZE), db.ForeignKey('room.key'), primary_key=True)
    ip = db.Column(db.String(IPV4_MAX_LENGTH), db.ForeignKey('user.ip'), primary_key=True)

    def __repr__(self):
        return 'Room: {}, User{}'.format(self.room, self.name)

db.create_all()
dummy_room = Room(key="",
                  host="dummy",
                  name="dummy_room",
                  log="",
                  mute=True,
                  file=None)
db.session.add(dummy_room)
db.session.commit()
"""
===============================================================================
"""

from source.route import main as main_blueprint
app.register_blueprint(main_blueprint)
socketio.init_app(app)
import source.events

if __name__ == '__main__':
    socketio.run(app)

