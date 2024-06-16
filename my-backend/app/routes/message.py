from flask import Blueprint, request, jsonify
from app.models import User, Message, Conversation

message_bp = Blueprint('message', __name__)

@message_bp.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    message_content = data.get('message_content')
    user_id = data.get('user_id')
    conversation_id = data.get('conversation_id')

    if not message_content or not user_id or not conversation_id:
        return jsonify({'error': 'Please provide message content, user ID, and conversation ID'}), 400

    message = Message(message_content=message_content, user_id=user_id, conversation_id=conversation_id)
    message.save()

    return jsonify({'message': 'Message sent successfully'}), 201

@message_bp.route('/<message_id>', methods=['GET'])
def get_message(message_id):
    message = Message.find_by_id(message_id)
    if message:
        return jsonify({
            'message_id': message.message_id,
            'message_content': message.message_content,
            'user_id': message.user_id,
            'conversation_id': message.conversation_id
        }), 200
    return jsonify({'error': 'Message not found'}), 404

@message_bp.route('/user/<user_id>', methods=['GET'])
def get_messages_by_user(user_id):
    messages = Message.find_by_user_id(user_id)
    return jsonify([
        {
            'message_id': msg.message_id,
            'message_content': msg.message_content,
            'user_id': msg.user_id,
            'conversation_id': msg.conversation_id
        } for msg in messages
    ]), 200
