import * as React from 'react';

import { Button } from './Button';
import { Socket } from './Socket';
import { GoogleButton } from './GoogleButton';

export function Content() {
    const [messages, setMessages] = React.useState([]);
    const [counts, setCounts] = React.useState([]);
    
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('messages received', updateMessages);
            return () => {
                Socket.off('messages received', updateMessages);
            };
        });
    }
    
    function getUserCount() {
        React.useEffect(() => {
            Socket.on('user count', updateCount);
            return () => {
                Socket.off('user count',updateCount);    
            };
        });
    }
    
    function updateMessages(data) {
        console.log("Received messages from server: "  + data['allMessages']);
        setMessages(data['allMessages']);
        let chatScroll = document.getElementById("scroll");
        chatScroll.scrollTop = chatScroll.scrollHeight;
    }
    
    function updateCount(data) {
        console.log("Received user count from server: " + data['allUserCount']);
        setCounts(data['allUserCount']);
    }
    
    getNewMessages();
    getUserCount();
    
    return (
        <div> 
            <h1>Chat Room</h1>
            <GoogleButton />
            <h2> Current users: {counts}</h2>
                <ul id="scroll">
                    {   
                        messages.map(
                        (message, index) => <li key={index}>{message}</li>)
                    }
                </ul>
            <Button />
        </div>
    );
}