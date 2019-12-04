// create instance of socket 
var socket = io.connect('http://localhost:5000/')

// check form data using jQuery 
var form = $('#chat-form').on("submit", function(e){
    e.preventDefault()
    var username = $("#username").val()
    var message = $("#message").val()
    console.log(username, message)
})