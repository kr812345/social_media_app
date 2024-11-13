from flask import request,jsonify
from dm_app.Services.chat_service import ChatService
from dm_app.Views.chat_view import Chatview                                               
from shared.models.chat_model import Chat,Content
from user_app.controllers.user_controller import UserController
from dm_app.Services.Cloud_services import CloudService

class ChatController:
    @staticmethod
    def get_all_chats(username):
        chats = ChatService.get_all_chats(username)
        return Chatview.render_chats(chats), 200

    @staticmethod
    def open_chat(chat_id):
        chat = ChatService.open_chat(chat_id)
        if not chat:
            return Chatview.render_error("chat_id not found."), 404
        return Chatview.render_chats(chat), 200

    @staticmethod
    def create_chat():
        data = request.get_json()
        chat_id = data.get('chat_id')
        sender_name = data.get('sender_name')
        receiver_name = data.get('receiver_name')
        follower = data.get('follower')
        content = data.get('content')

        chat = ChatService.create_chat(chat_id,sender_name,receiver_name, follower, content)
        if chat:
            return Chatview.render_success('Chat Created, Say hii..',chat.chat_id), 201
        return Chatview.render_error("User not found."), 404

    @staticmethod
    def delete_chat(chat_id):
        ChatService.delete_chat(chat_id)

        if not chat_id:
            return Chatview.render_error('chat_id does not exist.'), 404
        return Chatview.render_success("chat deleted", chat_id), 201

    @staticmethod
    def send_message():
        data = request.get_json()
        chat_id = data.get('chat_id')
        sender_name = data.get('sender_name')
        receiver_name = data.get('receiver_name')
        encrypted_content = ChatService.chat_encryption(data.get('content'))

        if Chat.query.filter_by(sender_name=sender_name) and Chat.query.filter_by(receiver_name=receiver_name):
            if encrypted_content:
                chat = ChatService.create_chat(chat_id = chat_id, sender_name = sender_name, receiver_name = receiver_name, follower = 1, content = encrypted_content)
                return Chatview.render_chat(chat), 200
        return Chatview.render_error('One of the chatting partner is missing.'), 401

    @staticmethod
    def receive_message(chat_id):
        if (Chat.query.filter_by(chat_id=chat_id).order_by(Chat.sent_at.desc()).first().sent_at < Content.query.filter_by(chat_id=chat_id).order_by(Content.uploaded_at.desc()).first().uploaded_at):
            latest_msg = Chat.query.filter_by(chat_id=chat_id).order_by(Chat.sent_at.desc()).first()

            decrypted_content = ChatService.chat_decryption(latest_msg.content)

            if decrypted_content:
                return Chatview.render_chat(latest_msg), 200
            
            return Chatview.render_error('decryption me koi dikkat h..'), 401
        
        else:
            latest_msg = Content.query.filter_by(chat_id=chat_id).order_by(Content.uploaded_at.desc()).first()

            decrypted_content = ChatService.chat_decryption(latest_msg.content_url)

            if decrypted_content:
                return Chatview.render_media(latest_msg), 200
            
            return Chatview.render_error('decryption me koi dikkat h..'), 401

    @staticmethod
    def get_profile(chat_id):
        profile = ChatService.get_profile(chat_id)

        if not profile:
            return Chatview.render_error('profile nhi h..'), 404
        
        return {"Username":profile['username'],"full_name":profile["full_name"],"followers":2,"bio":profile["bio"]}, 200



    @staticmethod
    def upload_media_file(chat_id):

        public_url = CloudService.select_file_dialog(chat_id)

        if (public_url):
            return (f"chat_id: {chat_id}, file sent successfully!, can find it on URL: { public_url }"), 200
        
        return Chatview.render_error('No file selected.')

    @staticmethod
    def get_uploaded_media():

        public_url = CloudService.get_uploaded_file_url()

        if public_url:
            return Chatview.render_success(f'required file url: {public_url}'), 200
        return Chatview.render_error('required url not found.'), 404

    @staticmethod
    def get_media(chat_id):
        content_type = ".jpg"
        if content_type == ".mp4" or ".mkv" or ".avi":
            return ChatService.get_videos(chat_id,content_type)
        if content_type == ".mp3":
            return ChatService.get_audios(chat_id,content_type)
        if content_type == ".jpg" or ".png" or ".svg" or ".webp":
            return ChatService.get_images(chat_id,content_type)

        return Chatview.render_error('chat not found or content_type is incorrect.'), 404