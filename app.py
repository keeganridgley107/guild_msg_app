"""
guild message app

author: keegan ridgley 

date: 12/04/19 
"""

from flask import Flask, render_template, request 
from flask_socketio import SocketIO, emit 
from bs4 import BeautifulSoup as Soup
import json 
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '^(p#PHi&^wF,W_KDTTH2#j' # needed to create instance of socketIO app 
socketio = SocketIO(app) # socketIO wrapper 

################# SOCKETIO ##################

@socketio.on('chat-message')
def handle_message(message):
    print("Got a Message!", str(message))
    # write messages to file for persistance? 
    
    # new idea: update html template with each msg emit
    # html_doc = open('templates/chat_page.html', 'w')
    # html_template = Soup(html_doc) # parse template
    # print(html_template)
    # template_message_window = html_template.find('div', {"id": "message-window"}) # find msg window
    # print(template_message_window)
    # new_tag = html_template.new_tag('div') # create new msg div
    # new_tag.attrs['class'] = 'well well-sm' # add class 
    # new_tag.append(message['username'] + ' : '+ message['data']) # add msg text
    # print(new_tag)
    # template_message_window.append(new_tag) # add new div to template 
    # html_doc.write(html_template)
    # html_doc.close()
    emit('message-response', message, broadcast=True)

@socketio.on('connection-event')
def handle_connection(json):
    print("Got a Connection!", str(json))
    emit('connection-response', json, broadcast=True)

################## ROUTES ###################
@app.route("/", methods=['GET', 'POST'])
def index():
    # if local file has data ==> load template with log msgs appended to msg window div
    # else, return the inital template
     
    # check if data file has contents  
    if os.path.getsize('data.txt') > 0:
        with open('data.txt') as json_file:
            data = json.load(json_file)
            # load the messages in the log file and emit them to poulate msg window
            for m in data['messages']:
                loaded_message = {
                    'username': m['username'],
                    'data': m['data']
                    }
                # emit but not broadcast to populate msg window ==> namespace error?
                # emit('chat-message', loaded_message) 

                print('Username: ' + m['username'])
                print('Message: ' + m['data'])
                print('')
        pass

    return render_template('./chat_page.html')

if __name__ == "__main__":
    socketio.run(app, debug=True) # socketIO wrapper starts flask server 