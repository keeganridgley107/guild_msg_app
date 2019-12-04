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
socket.on('message-response', function(respMessage){
    if ($('#empty-msg').length){
        $('#empty-msg').remove()
    }
    $('#message-window').append('<div class="well well-sm">'+ respMessage.username + ' : '+ respMessage.data +'</div>')
    console.log("newMsg", respMessage)
})

// submit form data using jQuery 
var form = $('#chat-form').on("submit", function(e){
    e.preventDefault()
    var message = $('#chat-msg').val()
    var username = $('#username').val()
    // clear the inputs for next msg 
    $("#chat-msg").val("") 
    
    // send message and username 
    socket.emit('chat-message', {
        'username': username,
        'data': message
    })
})