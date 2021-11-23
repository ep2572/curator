"""
===============================================================================
# Models for the database
# Clients(Many) to Rooms(Many)
===============================================================================
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

KEY_SIZE = 12
IPV4_MAX_LENGTH = 15


class Room(db.Model):
    """
    A rooms only exists so long as 1 Client is still present. Each room
    will maintain the chat log,
    """
    key = db.Column(db.String(KEY_SIZE), primary_key=True)
    host = db.Column(db.String(IPV4_MAX_LENGTH), nullable=False)
    name = db.Column(db.String(512), default='curator room '+key)
    log = db.Column(db.Text, default='')
    mute = db.Column(db.Boolean, default=False)
    file = db.Column(db.LargeBinary)

    def __repr__(self):
        return '{}, {}'.format(self.name, self.key)


class Client(db.Model):
    """
    A client can be in multiple rooms at once, with different names,
    colors, and roles. A new instance of the client class is given
    to the client for each room the are in.
    """
    ip = db.Column(db.String(IPV4_MAX_LENGTH), primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    # role: 0 is guest, 1 is moderator, 2 is host
    role = db.Column(db.SmallInteger, default=0)
    # Default color is Black 0x000000
    color = db.Column(db.String(6), default='000000', nullable=False)
    in_room = db.Column(db.String(KEY_SIZE), db.ForeignKey('room.key'),
                        primary_key=True)

    def __repr__(self):
        return 'Client: {}:{}, Role: {}'.format(self.name, self.ip, self.role)


class Banlist(db.Model):
    """
    Each instance of the Banlist has only one room and one client IP
    """
    room = db.Column(db.String(KEY_SIZE),
                     db.ForeignKey('room.key'),
                     primary_key=True)
    client = db.Column(db.String(IPV4_MAX_LENGTH),
                       db.ForeignKey('client.ip'),
                       primary_key=True)

    def __repr__(self):
        return 'Room: {}, IP{}'.format(self.room, self.client)
