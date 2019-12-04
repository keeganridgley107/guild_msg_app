# guild_msg_app
quick little messaging app written in python 

## How to run
Copy and paste the following commands into a terminal: 
```
git clone https://github.com/keeganridgley107/guild_msg_app.git && cd guild_msg_app/ && python3 -m venv guild_msg_venv && source guild_msg_venv/bin/activate && pip install -r requirements.txt && python app.py
```
The chat server is now running on localhost port 5000 (127.0.0.1:5000)

## How to connect

to connect as a client and begin chatting open any browser and navigate to `localhost:5000`


- Goal: 
    - An application that allows two users to send short text messages to each other

- Guidelines: 
    - Don't spend much time  
    - no accounts, users, registration, graphics or visual appeal 
    - it's perfectly fine to have one or two "hardcoded" accounts that simply work with each other


### Notes

- will likely need socket to broadcast / recieve messages
    - flask-socketio seems like better choice if I decide to add flask front end 
- pip version is not current, update if issues arise
- decided I'm going with flask/ socketIO to add front end to chat server 
    - challenge myself with db once mvp is working
- front end is hard. 
    - just spent too much time on centering columns and text, taking the dog out to refocus 

- todo
    - socket is showing conns from multiple clients but not emiting msg responses to multiple clients 
        - SOLVED: broadcast flag would help on the emits!
    - tried to use json as quick db solution but it failed to prove any easier than sqlite 
        - emit causes namespace error when hit with loaded_messages in index()
    
