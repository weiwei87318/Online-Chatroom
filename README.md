
Online Chatroom
=======

Demo: https://pacific-island-24462.herokuapp.com/

1. Install your stuff!    
  a) `npm install`    
  b) `pip install flask-socketio`    
  c) `pip install eventlet`    
  d) `npm install -g webpack`    
  e) `npm install --save-dev webpack`    
  f) `npm install socket.io-client --save`
  g) `npm install react-google-login`
2. Create sql.env with DATABASE_URL in it.
3. Run your code!    
  a) `sudo sudo service postgresql start` and `npm run watch`. If prompted to install webpack-cli, type "yes"    
  b) In a new terminal, `python app.py`    
  c) Preview Running Application (might have to clear your cache by doing a hard refresh) 

#Technical issues during building the app: <br>
  Although, it's just adding google OAuth in milestone 2, but it suffers me a lot for figuring out how to combine name and message in to the database. In the beginning, I was trying to send both name and message from the button and it turns out not to work. So I ask my one of my classmate Jacob, he gave me an idea of using dictionary and set the key to `request.sid`, username to value. So I just figure it out it is basically same as milestone 1 but I'm just thinking it too hard. The second problem I had is during making changes of code, I had an issue which my app keep refreshing everytime I try to send message. I fix it by redo and just try to find another way. The third problem I have is after I push my app to heroku, in the beginning it is fine, but before I was submitting the project form, when I was trying to login with my google account, the page just did nothing.

#Improvements can be done in future: <br>
  I take really few time on the css styling, in the beginning I was trying to make the interface clean and simple, but after I finish the project I feel it's a bit boring. So in the future I think I can take more time on the styling part.
