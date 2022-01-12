from os.path import join, dirname
from dotenv import load_dotenv
from flask import request
import os
import flask
import flask_sqlalchemy
import flask_socketio
import models

MESSAGE_RECEIVED_CHANNEL = 'messages received'
USERS_UPDATED_CHANNEL = 'accounts received'
USER_COUNT = 'user count'

app = flask.Flask(__name__)

#sockectio init
socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

#sql
dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

#database config
database_uri = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app
db.create_all()
db.session.commit()

#count connected User
user_names = {}

def emit_all_oauth_users(channel):
    all_Accounts = [ \
        user.name for user \
        in db.session.query(models.AuthUser).all()]
        
    socketio.emit(channel, {
        'allAccounts':all_Accounts
    })

def push_new_user_to_db(name, auth_type):
    db.session.add(models.AuthUser(name,auth_type));
    db.session.commit();
    emit_all_oauth_users(USERS_UPDATED_CHANNEL)
    

def emit_all_messages(channel):
    all_Messages = [ \
        db_message.messages for db_message in \
        db.session.query(models.Chatroom).all()]
        
    socketio.emit(channel, {
        'allMessages': all_Messages
    })

def emit_all_userCount(channel):
    allUserCount = len(user_names);
    socketio.emit(channel, {
        'allUserCount': allUserCount   
    })
    
@socketio.on('connect')
def on_connect():
    print( 'Someone connected!')
    emit_all_oauth_users(USERS_UPDATED_CHANNEL)
    emit_all_userCount(USER_COUNT)
    
@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')
    del user_names[request.sid]
    print(user_names)
    print(len(user_names))
    emit_all_userCount(USER_COUNT)
    
@socketio.on('new google user')
def on_new_google_user(data):
    user_names[request.sid] = data['name']
    print("Got an event for new google user input with data:", data)
    print(user_names)
    push_new_user_to_db(data['name'], models.AuthUserType.GOOGLE)
    
    emit_all_userCount(USER_COUNT)
    
    
@socketio.on('new_message_received')
def on_new_message(data):
    print("Got an event for new message input with data: " +  data["messages"])
    db.session.add(models.Chatroom(user_names[request.sid] + " : " + data["messages"]));
    db.session.commit();
    if data["messages"] == "!! about":
        db.session.add(models.Chatroom("[ ChatBot ] : Welcome to CS490 project 2 chat room"));
        db.session.commit();
    elif data["messages"] == "!! help":
        db.session.add(models.Chatroom("[ ChatBot ] : Here is a list of command - !! about , !! help , !! funtranslate"));
        db.session.commit();
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)

@app.route('/')
def index():
    emit_all_oauth_users(USERS_UPDATED_CHANNEL)
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)

    return flask.render_template("index.html")

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )