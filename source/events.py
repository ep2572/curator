from flask import session
from flask_socketio import emit, join_room, leave_room
from .socket import socketio


@socketio.on('connect', namespace='/chat')
def connect():
    print('successfully connected!')


@socketio.on('join', namespace='/chat')
def join(information):
    room_name = information.get('client_to_server')
    user_name = session.get('user_name')
    join_room(room_name)
    emit('status', {'server_to_client': user_name + ' enter the room'}, room=room_name)


@socketio.on('leave', namespace='/chat')
def leave(information):
    room_name = information.get('client_to_server')
    user_name = session.get('user_name')
    leave_room(room_name)
    emit('status', {'server_to_client': user_name + ' has left the room'}, room=room_name)


@socketio.on('text', namespace='/chat')
def text(information):
    room_name = information.get('client_to_server')
    text = information.get('text')
    user_name = session.get('user_name')
    emit('message', {
        'user_name': user_name,
        'text': text,
    }, room=room_name)


