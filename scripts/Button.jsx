import * as React from 'react';
import { Socket } from './Socket';

function handleSubmit(event) {
    
    let newMessage = document.getElementById("message_input");
    Socket.emit('new_message_received', 
        {'messages': newMessage.value,'name':'testusername'} ,
    ); 
    
    newMessage.value
    
    console.log( 'Sent the message ' + newMessage.value + ' to server!');
    newMessage.value = ''
    
    
    event.preventDefault();
}

export function Button() {
    return (
        
        <form onSubmit={handleSubmit}>
            <input id="message_input" placeholder="Enter a message"></input>
            <button>send</button>
        </form>
    );
}
