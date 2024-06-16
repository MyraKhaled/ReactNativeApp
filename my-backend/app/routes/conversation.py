from flask import Blueprint, request, jsonify
from app.models import User, Message, Conversation

conversation_bp = Blueprint('conversation', __name__)

@conversation_bp.route('/create', methods=['POST'])
def create_conversation():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_id = data.get('user_id')

    if not title or not content or not user_id:
        return jsonify({'error': 'Please provide title, content, and user ID'}), 400

    conversation = Conversation(title=title, content=content, user_id=user_id)
    conversation.save()

    return jsonify({'message': 'Conversation created successfully'}), 201

@conversation_bp.route('/<conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    conversation = Conversation.find_by_id(conversation_id)
    if conversation:
        return jsonify({
            'conversation_id': conversation.conversation_id,
            'title': conversation.title,
            'date': conversation.date,
            'content': conversation.content,
            'user_id': conversation.user_id
        }), 200
    return jsonify({'error': 'Conversation not found'}), 404

@conversation_bp.route('/user/<user_id>', methods=['GET'])
def get_conversations_by_user(user_id):
    conversations = Conversation.find_by_user_id(user_id)
    return jsonify([
        {
            'conversation_id': conv.conversation_id,
            'title': conv.title,
            'date': conv.date,
            'content': conv.content,
            'user_id': conv.user_id
        } for conv in conversations
    ]), 200

