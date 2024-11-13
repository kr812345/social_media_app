from flask import jsonify
from shared.models.chat_model import Chat, Content
from dm_app.Views.chat_view import Chatview
from shared.models.user_model import User
from shared.utils.db_utils import db
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64
import os

class ChatService:
    @staticmethod
    def create_chat(chat_id,sender_name,receiver_name,follower,content):
        if User.query.filter_by(username=sender_name).first() and User.query.filter_by(username=receiver_name).first():
            if (follower == 1):
                new_chat = Chat( 
                    chat_id = chat_id,
                    sender_name = sender_name,
                    receiver_name = receiver_name,
                    follower = follower,
                    content = ChatService.chat_encryption(content)
            )
            db.session.add(new_chat)
            db.session.commit()
            return new_chat

    @staticmethod
    def delete_chat(chat_id):
        chats = Chat.query.filter_by(chat_id = chat_id).all()
        for chat in chats:
            db.session.delete(chat)
            db.session.commit()

    @staticmethod
    def get_all_chats(username):
        chats = Chat.query.filter_by(sender_name=username).all()
        return chats

    @staticmethod
    def open_chat(chat_id):
        if chat_id:
            return Chat.query.filter_by(chat_id = chat_id).all()


    @staticmethod
    def chat_encryption(content):
        
        if isinstance(content, str):
            content = content.encode('utf-8')

        key = os.urandom(32)
        
        iv = os.urandom(16)

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_content = padder.update(content) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        cipher_content = encryptor.update(padded_content) + encryptor.finalize()

        key_iv_cipher_content = key + iv + cipher_content
        
        return key_iv_cipher_content

    @staticmethod
    def chat_decryption(key_iv_cipher_content):
        
        key = key_iv_cipher_content[:32]
        iv = key_iv_cipher_content[32:48]
        cipher_content = key_iv_cipher_content[48:]

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_padded_content = decryptor.update(cipher_content) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_content = unpadder.update(decrypted_padded_content) + unpadder.finalize()

        return decrypted_content.decode('utf-8')

    @staticmethod
    def get_profile(chat_id):
        if chat_id:
            chats = Chat.query.filter_by(chat_id = chat_id).all()
            username = chats[0].receiver_name
            user = User.query.filter_by(username = chats[0].receiver_name).first()
            
            if user:
                full_name = user.full_name
                bio = user.bio
            
                profile = {
                    "username":username,
                    "full_name":full_name,
                    "bio":bio
                    }
                return profile

    @staticmethod
    def get_videos(chat_id,content_type=".mp4"):
        if Chat.query.filter_by(chat_id = chat_id).first():
            content = Content.query.filter_by(content_type = content_type)
            return Chatview.render_media(content)

    @staticmethod
    def get_audios(chat_id,content_type='.mp3'):
        if Chat.query.filter_by(chat_id = chat_id).first():
            content = Content.query.filter_by(content_type = Content_type)
            return Chatview.render_media(content)

    @staticmethod
    def get_images(chat_id,content_type='.jpg' or '.png'):
        if Chat.query.filter_by(chat_id = chat_id).first():
            content = Content.query.filter_by(content_type = Content_type)
            return Chatview.render_media(content)
