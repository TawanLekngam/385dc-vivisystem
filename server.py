from flask import Flask, request
from flask_socketio import SocketIO, emit
from models import EventType

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect(data):
    pond = request.args.get('pondId')
    print(f"{pond} connects")

@socketio.on('disconnect')
def handle_disconnect():
    pond = request.args.get('pondId')
    print(f"{pond} disconnects")
    emit(str(EventType.DISCONNECT), pond, broadcast=True)

@socketio.on(str(EventType.MIGRATE))
def handle_migrate(destination, data):
    pond = request.args.get('pondId')
    print(f'received migrate from {pond}, data: {data}')
    emit(str(EventType.MIGRATE), (destination, data), broadcast=True)

@socketio.on(str(EventType.STATUS))
def handle_status(data):
    pond = request.args.get('pondId')
    print(f'received status from: {pond}, data: {data}')
    emit(str(EventType.STATUS), data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)