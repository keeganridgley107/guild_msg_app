console.log("loaded js! ")


// create instance of socket when user loads page
var socket = io.connect('http://localhost:5000/')
// create message when user joins
socket.on('connect', function(){
    socket.emit('connection-event', {
        data: 'New Connection'
    })
})

// listen for new connections
socket.on('connection-response', function(json){
    console.log("NewUser", json)
})

// listen for new messages
socket.on('message-response', function(message){
    console.log("newMsg", message)
})

// submit form data using jQuery 
var form = $('#chat-form').on("submit", function(e){
    e.preventDefault()
    var message = $("#chat-msg").val()
    
    // clear the inputs for next msg 
    $("#chat-msg").val("") 
    $("#username").val("")
    
    // send message and username 
    socket.emit('message', {
        'username': username,
        'message': message
    })
})