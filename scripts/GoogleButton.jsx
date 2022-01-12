import * as React from 'react';
import { Socket } from './Socket';
import ReactDOM from 'react-dom';
import GoogleLogin from 'react-google-login';


function handleSubmit(response) {
    console.log(response)
    let name = response.profileObj.email;
    Socket.emit('new google user', {
        'name': name,
    });
    
    console.log('Sent the name ' + name + ' to server!');
}

export function GoogleButton() {
    return <GoogleLogin
        clientId="733428808684-q5mj9ln7idk8aq6nidgghgnckag3tu7p.apps.googleusercontent.com"
        buttonText="Login"
        onSuccess={handleSubmit}
        onFailure={handleSubmit}
        cookiePolicy={'single_host_origin'}/>;

}
