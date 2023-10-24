import socketio

sio = socketio.Client(logger=True, engineio_logger=True)
sio.connect('http://localhost:5000')


@sio.on('response')
def response(data):
    print(data)  # {'from': 'server'}


@sio.on('message')
def response(data):
    print(data)  # {'from': 'server'}


sio.wait()
