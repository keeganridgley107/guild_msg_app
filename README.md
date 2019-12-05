# guild_msg_app
A quick little messaging app 

Made with a Python server and SocketIO
## How to run

Copy and paste the following commands into a terminal: 
```
git clone https://github.com/keeganridgley107/guild_msg_app.git && cd guild_msg_app/ && python3 -m venv guild_msg_venv && source guild_msg_venv/bin/activate && pip install -r requirements.txt && python app.py
```
The chat server is now running on localhost port 5000 (127.0.0.1:5000)

## How to connect
The easiest way to demo the app is to open two separate browser windows side-by-side and navigate both of them to `localhost:5000` 

### Goal:
Build an application that allows two users to send short text messages to each other
- Guidelines: 
    - Don't spend too much time (4 - 6 hours)
    - no accounts, users, registration, graphics or visual appeal 
    - it's perfectly fine to have one or two "hardcoded" accounts that simply work with each other

### Notes while coding
- will likely need socket to broadcast/receive messages in real-time 
    - flask-socketio seems like a better choice if I decide to add flask front end 
    - using python for my server makes sense for this, as does flask to manage routes 
- pip version is not current, update if issues arise
- decided I'm going with flask/ socketIO to add front end to chat server 
    - I will challenge myself with db once socket mvp is working but I think I should be fine using local memory and json, or csv file 
- front end is hard. 
    - I saved a bit of time by starting from a bootstrap docs forms example which I used as the basis for my message and username inputs (https://getbootstrap.com/docs/4.0/components/forms/) but still spent too much time adjusting trying to make my columns side by side 
    - SOLVED: columns require the parent element to be class row. 
    - taking the dog out to refocus 
- socket is showing connections from multiple clients but not emitting msg responses to multiple clients 
    - SOLVED: broadcast flag would help on the emits!
- a potential issue with json idea, emit throws error 
    - emit causes namespace error when hit with loaded_messages in index()
- I focused on real-time communications first with socket design, would have been smart to implement storage earlier in retrospect

### Todo
- I tried to use local json file as a quick storage solution but it failed to provide a benefit 
    - time/memory trade-off of json insert & load will end up awful at scale 
- using a local csv file, hashtable or an actual sqlite db would all be better long term solutions 
    - possible workaround solution for message storage is to update the template html once messages have been appended to message-window div 
    - tried using bs4 but encountered error with type not being string, a possible solution would add step to read, update, close, to parse html
- would have been cool to leverage more socketio funcationality to allow users to create named chatrooms 
- also with local storage I also would have liked to add the ability to prevent dupelicate usernames and save usernames

### Summary
When I initially read the prompt and saw the timeline/complexity advised I thought focusing on real-time communication driven by socketio would be a good solution based on experience using it in the past with javascript projects. I found a python pkg that integrated flask and socketio and thought that would work, the docs for flask_socketio demonstrated the use of custom emitters which I used to emit and listen for events between the python server and the html / javascript frontend. once I had achieved two-way communication using socketio I attempted to add chat persistence to the app, I had planned initially to use local memory in my python server since the scope was small enough. This proved more difficult than I initially thought since I tried to use json which as I mentioned above wouldn't scale and didn't end up working anyway due to issues I couldn't resolve with socketio's emit function. 

I wanted to hold myself to the timeline in the prompt and not go overboard but if I had more time to improve the chat app I would like to add persistence. First I would use a python object to store messages when they are handled in python. Then When the object reaches a preset size in memory have a python function write the object's message and user data to a text file stored locally on the server. I would then add a function to load the data (chats history) from the python object when a new user connects to the app and update their browser's DOM accordingly. 