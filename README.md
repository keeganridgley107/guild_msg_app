# guild_msg_app
quick little messaging app written in python 


- Goal: 
    - An application that allows two users to send short text messages to each other

- Guidelines: 
    - Don't spend much time  
    - no accounts, users, registration, graphics or visual appeal 
    - it's perfectly fine to have one or two "hardcoded" accounts that simply work with each other


### Thoughts 

- will likely need socket to broadcast / recieve messages
    - flask-socketio seems like better choice if I decide to add flask front end 
- pip version is not current, update if issues arise
- decided I'm going with flask/ socketIO to add front end to chat server 
    - challenge myself with db once mvp is working
- front end is hard. 
    - just spent too much time on centering columns and text, taking the dog out to refocus 

- todo
    - socket is showing conns from multiple clients but not emiting msg responses to multiple clients 