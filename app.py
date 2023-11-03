from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True)


if __name__ == "__main__":
    app.run(debug=True)

