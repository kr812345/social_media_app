from flask import Blueprint
from dm_app.Controllers.chat_controller import ChatController
from flask import request

chat_bp = Blueprint('chat_bp',__name__)

@chat_bp.route('/chats/<username>', methods=['GET'])
def get_all_chats(username):
    return ChatController.get_all_chats(request.args.get(username))

@chat_bp.route('/chats/<chat_id>', methods=['GET'])
def open_chat(chat_id):
    return ChatController.get_chat(request.args.get(chat_id))

@chat_bp.route('/create_chat', methods=['POST'])
def create_chat():
    return ChatController.create_chat()

@chat_bp.route('/chat/<chat_id>/<content>', methods=['POST'])
def send_message():
    return ChatController.send_message()

@chat_bp.route('/chat/<chat_id>', methods=['POST'])
def receive_message():
    return ChatController.receive_message()

# @chat_bp.route('/chat/<chat_id>/profile', methods=['GET'])
# def get_profile():
#     return ChatController.get_profile()

@chat_bp.route('/chat/<chat_id>/media', methods=['GET'])
def get_media():
    return ChatController.get_media()