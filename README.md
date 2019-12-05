# guild_msg_app
quick little messaging app written in python 

## How to run
Copy and paste the following commands into a terminal: 
```
git clone https://github.com/keeganridgley107/guild_msg_app.git && cd guild_msg_app/ && python3 -m venv guild_msg_venv && source guild_msg_venv/bin/activate && pip install -r requirements.txt && python app.py
```
The chat server is now running on localhost port 5000 (127.0.0.1:5000)

## How to connect

The easiest way to demo the app is to open two seperate browser windows side-by-side and navigate both of them to `localhost:5000` 

### Goal:

Build an application that allows two users to send short text messages to each other

- Guidelines: 
    - Don't spend much time  
    - no accounts, users, registration, graphics or visual appeal 
    - it's perfectly fine to have one or two "hardcoded" accounts that simply work with each other


### Notes while coding

- will likely need socket to broadcast / recieve messages
    - flask-socketio seems like better choice if I decide to add flask front end 
- pip version is not current, update if issues arise
- decided I'm going with flask/ socketIO to add front end to chat server 
    - challenge myself with db once mvp is working
- front end is hard. 
    - just spent too much time on centering columns and text, taking the dog out to refocus 
- socket is showing connections from multiple clients but not emiting msg responses to multiple clients 
    - SOLVED: broadcast flag would help on the emits!
- emit causes namespace error when hit with loaded_messages in index()

### Todo

- tried to use local json file as quick storage solution but it failed to provide a benefit 
    - time / memory trade off of json insert & load will likely end up worse at scale
        - using a local csv file, hashtable or an actual sqlite db would be more optimal long term solutions 
- focused on real time communications first with socket design, would have been smart to implement storage earlier in retrospect
- possible work-around solution for message storage is to update the template html once messages have been appended to message-window div    
    - tried using bs4 but encountered error with type not being string, possible solution would add step to read, update, close, to parse html