from datetime import datetime
from app import mongo

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save(self):
        user_data = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }
        mongo.db.users.insert_one(user_data)

class Message:
    def __init__(self, message_content, user_id, conversation_id):
        self.message_content = message_content
        self.user_id = user_id
        self.conversation_id = conversation_id

    def save(self):
        message_data = {
            'message_content': self.message_content,
            'user_id': self.user_id,
            'conversation_id': self.conversation_id,
            'created_at': datetime.now()
        }
        mongo.db.messages.insert_one(message_data)

class Conversation:
    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def save(self):
        conversation_data = {
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id,
            'created_at': datetime.now()
        }
        mongo.db.conversations.insert_one(conversation_data)


