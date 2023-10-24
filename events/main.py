from flask_restful import Api

from event_api import EventAPI
from event_routes import flask_app, socketio

api = Api(flask_app)
api.add_resource(EventAPI, "/events/<int:event_id>", endpoint='event')


@socketio.on('connect')
def handle_connection():
    print('Someone connected')
    socketio.emit('message', 'A user has joined')


@flask_app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    socketio.run(flask_app, debug=True, port=5000, allow_unsafe_werkzeug=True)
