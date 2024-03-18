from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('mensaje')
def handle_mensaje(msg):
    print(msg)
    socketio.emit('mensaje', msg)

if __name__ == "__main__":
    socketio.run(app, debug=True) 
