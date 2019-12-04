"""
guild message app

author: keegan ridgley 

date: 12/04/19 
"""

from flask import Flask, render_template 
from flask_socketio import SocketIO  


app = Flask(__name__)
app.config['SECRET_KEY'] = '^(p#PHi&^wF,W_KDTTH2#j' # needed to create instance of socketIO app 
socketio = SocketIO(app) # socketIO wrapper 


@app.route("/")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    socketio.run(app, debug=True) # socketIO wrapper starts flask server