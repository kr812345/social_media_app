from flask import Blueprint, request
from dm_app.Controllers.chat_controller import ChatController

chat_bp = Blueprint('chat_bp',__name__)

@chat_bp.route('/chats/<username>', methods=['GET'])
def get_all_chats(username):
    return ChatController.get_all_chats(username)

@chat_bp.route('/chat/<int:chat_id>', methods=['GET'])
def open_chat(chat_id):
    return ChatController.open_chat(chat_id)

@chat_bp.route('/create_chat', methods=['POST'])
def create_chat():
    return ChatController.create_chat()

@chat_bp.route('/delete_chat/<int:chat_id>', methods=['GET'])
def delete_chat(chat_id):
    return ChatController.delete_chat(chat_id)

@chat_bp.route('/chat/send_message', methods=['POST'])
def send_message():
    return ChatController.send_message()

@chat_bp.route('/<int:chat_id>/receive_message', methods=['GET'])
def receive_message(chat_id):
    return ChatController.receive_message(chat_id)

@chat_bp.route('/<int:chat_id>/profile', methods=['GET'])
def get_profile(chat_id):
    return ChatController.get_profile(chat_id)

@chat_bp.route('/chat/<int:chat_id>/send_media', methods=['GET'])
def send_media(chat_id):
    return ChatController.upload_media_file(chat_id)

@chat_bp.route('/<int:chat_id>/get_media', methods=['GET'])
def get_media(chat_id):
    return ChatController.get_media(chat_id)