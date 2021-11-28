from flask import Flask, session
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from flask_socketio import rooms
import socketio

app = Flask(__name__)

socketIo = SocketIO(app, cors_allowed_origins="*")

app.debug = True

app.host = 'localhost'

@socketIo.on('join')
def on_join(data):
    username = data['user']
    room = data['room']
    join_room(room)
    send(f'{username} has entered the room {room}', to=room)


@socketIo.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)


@socketIo.on('connect')
def test_connect(auth):
    emit('my response', {'data': 'Connected'})

@socketIo.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketIo.on("message")
def handleMessage(msg):
    print(msg)
    send(msg, to=rooms())

    return None

    

if __name__ == '__main__':
    socketIo.run(app)
