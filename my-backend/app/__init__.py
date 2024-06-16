from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
app.config['MONGO_URI'] = 'mongodb://localhost:27017/chatbotDB'
app.config['SECRET_KEY'] = '89a43b725aa4988ffa02586623dda2d862cd38c15bd5921af20fa0a23f0e19cc'

mongo = PyMongo(app)

from app.routes.auth import auth_bp
from app.routes.message import message_bp
from app.routes.conversation import conversation_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(message_bp, url_prefix='/api/messages')
app.register_blueprint(conversation_bp, url_prefix='/api/conversations')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


