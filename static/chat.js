console.log("loaded js! ")
// create instance of socket when user loads page
var socket = io.connect('http://localhost:5000/')
// create message when user joins
socket.on('connect', function(){
    socket.emit()
})
// check form data using jQuery 
var form = $('#chat-form').on("submit", function(e){
    e.preventDefault()
    var username = $("#username").val()
    var message = $("#chat-msg").val()
    console.log(username, message)
})