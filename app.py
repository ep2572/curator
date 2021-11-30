from flask import Flask, render_template, redirect, request, session, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
from source.model import db, Room, Client, Banlist
from source.roomkey import get_roomkey
import os

app = Flask(__name__)
#app.secret_key = os.environ.get('SECRET')
app.secret_key = 'adfsjodanf'
app.config['SECRET_KEY'] = 'adfsjodanf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql' + os.environ.get('DATABASE_URL')[8:]

# Generate database with dummy room
db.init_app(app)
app.app_context().push()
db.create_all()
dummy_room = Room(key="dummy",
                  host="dummy",
                  name="dummy_room",
                  cap=32,
                  note="",
                  log="This is the dummy room. The room you are looking for doesn't exist.",
                  mute=True,
                  file=None)
db.session.add(dummy_room)
db.session.commit()

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        session['user_name'] = name
        return redirect(url_for('.chat'))
    return render_template('home.html')


@app.route('/chat/<string:room_key>', methods=['GET', 'POST'])
def chat(room_key):
    
    return render_template('chat.html')
    

@app.route('make_room', methods=['GET', 'POST'])
def make_room():
    roomkey = get_roomkey()
    user_ip = request.remote_addr
    username = request.form['user_name']
    roomname = request.form['room_name']
    capacity = request.form['capacity']
    notice = request.form['note']
    new_room = Room(key=roomkey,
                    host=ip,
                    name=roomname,
                    cap=capacity,
                    note=notice)
    db.session.add(new_room)
    db.session.commit()
    new_user = Client(ip = user_ip,
                      name = username,
                      role = 2,
                      color = '000000',
                      in_room = new_room)
    db.session.add(new_user)
    db.session.commit()
    return url_for('chat', room_key=roomkey, room = new_room, user = new_user)


@socketio.on('connect')
def connect():
    print('successfully connected!')


@socketio.on('join')
def join(information):
    room_name = information.get('client_to_server')
    user_name = session.get('user_name')
    join_room(room_name)
    emit('status', {'server_to_client': user_name + ' enter the room'}, room=room_name)


@socketio.on('leave')
def leave(information):
    room_name = information.get('client_to_server')
    user_name = session.get('user_name')
    leave_room(room_name)
    emit('status', {'server_to_client': user_name + ' has left the room'}, room=room_name)


@socketio.on('text')
def text(information):
    room_name = information.get('client_to_server')
    text = information.get('text')
    user_name = session.get('user_name')
    emit('message', {
        'user_name': user_name,
        'text': text,
    }, room=room_name)


@socketio.on('mouse')
def mouse(data):
    # room_name = data.get('client_to_server')
    socketio.emit('drawing', data)


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json)

if __name__=="__main__":
    app.run()
