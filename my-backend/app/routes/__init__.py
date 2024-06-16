from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
message_bp = Blueprint('message', __name__)
conversation_bp = Blueprint('conversation', __name__)

from . import auth, message, conversation  # Import route modules
