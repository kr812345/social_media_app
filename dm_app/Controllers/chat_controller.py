from flask import request
from dm_app.Services.chat_service import ChatService
from dm_app.Views.chat_view import Chatview
from shared.models.chat_model import Chat

class ChatController:
    @staticmethod
    def get_all_chats(username):
        chats = ChatService.get_all_chats(username)
        return Chatview.render_chats(chats), 200

    @staticmethod
    def get_chat(chat_id):
        chat = ChatService.open_chat(chat_id)
        if not Chat.follower:
            return Chatview.render_error("They don't follow you."), 404
        return Chatview.render_chat(chat), 200

    @staticmethod
    def create_chat():
        data = request.get_json()
        chat_id = data.get('chat_id')
        sender_name = data.get('sender_name')
        receiver_name = data.get('receiver_name')
        content_type = data.get('content_type')
        content = data.get('content')
        receiver_at = data.get('receiver_at')

        chat = ChatService.create_chat(sender_name,receiver_name, content_type, content)
        return Chatview.render_success('Chat Created, Say hii..',chat_id), 201

    @staticmethod
    def delete_chat(chat_id):
        chat_id = request.get('chat_id')
        ChatService.delete_chat(chat_id)
        return 

    @staticmethod
    def send_message():
        data = request.get_json()
        sender_name = data.get('sender_name')
        receiver_name = data.get('receiver_name')
        content_type = data.get('content_type')
        encrypted_content = ChatService.chat_encryption(data.get('content'))

        if encrypted_content:
            return Chatview.render_success('pta ni kya kru iske baad!'), 200
        return Userview.render_error('Kux error aaya h..'), 401

    @staticmethod
    def receive_message():
        data = request.get_json()
        sender_name = data.get('sender_name')
        receiver_name = data.get('receiver_name')
        content_type = data.get('content_type')
        decrypted_content = data.get('encrypted_content')

        if decrypted_content:
            return Chatview.render_success('naa-samajhne se samajhne me privartan ho gya h..'), 200
        return Chatview.render_error('samajhna suljhane me koi dikkat h..'), 401

    # @staticmethod
    # def get_profile():
    #     data = request.get_json()
    #     receiver_name = data.get('receiver_name')
    #     profile = ChatService.get(receiver_name)

    #     if profile:
    #         return Chatview.render_success('profile mil gyi..'), 200
    #     return Chatview.render_error('profile milne me koi dkkt h..'), 404

    @staticmethod
    def get_media():
        data = request.get_json()
        chat_id = data.get('chat_id')
        content_type = data.get('content_type')
        content = data.get("content")
        if content_type == mp4:
            return ChatService.get_videos(chat_id,content_type)
        if content_type == mp3:
            return ChatService.get_audios(chat_id,content_type)
        if content_type == jpg or png:
            return ChatService.get_images(chat_id,content_type)

        return Chatview.render_error('chat not found or content_type is incorrect.'), 404
        
    @staticmethod
    def upload_media_file():
        return

    @staticmethod
    def delete_chat(chat_id):
        if chat_id:
            db.session.delete(open_chat(chat_id))
            db.session.commit()