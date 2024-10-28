from shared.models.chat_model import Chat,Content
from shared.models.user_model import User
from shared.utils.db_utils import db
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

class ChatService:
    @staticmethod
    def create_chat(sender_name,receiver_name,content_type,content):
        if (Chat.follower):
            new_chat = Chat(
                sender_name = sender_name,
                receiver_name = receiver_name,
                content_type = content_type,
                content = content
        )
        db.session.add(new_chat)
        db.session.commit()
        return new_chat

    @staticmethod
    def get_all_chats(username):
        print(username)
        return Chat.query.filter(username = username).all()

    @staticmethod
    def open_chat(chat_id):
        if chat_id:
            return Chat.query.filter_by(chat_id = chat_id).first()


    @staticmethod
    def chat_encryption(content):
        
        key = os.urandom(32)
        
        iv = os.urandom(16)

        padder = padding.PKCS7(algorithms.AEC.block_size).padder()
        padded_content = padder.update(content.encode('utf-8')) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        cipher_content = enryptor.update(padded_content) + encyptor.finalize()

        return cipher_content

    def chat_decryption(cipher_content, key, iv):

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default.finalize())
        decryptor = cipher.decryptor()

        decrypted_padded_content = decryptor.update(cipher_content) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_content = unpadder.update(decrypted_padded_content) + unpadder.finalize()

        return decrypted_content.decode('utf-8')

    # @staticmethod
    # def get_profile(receiver_name):
    #     profile = print("get this from khushdeep!")
    #     return "profile return hogi..!"

    @staticmethod
    def get_videos(chat_id,content_type="mp4"):
        if Chat.query.filter_by(Chat.chat_id == chat_id).first():
            return Content.query.filter_by(content_type = content_type)

    @staticmethod
    def get_audios(chat_id,content_type='mp3'):
        if Chat.query.filter_by(Chat.chat_id == chat_id).first():
            return Content.query.filter_by(content_type = Content_type)

    @staticmethod
    def get_photos(chat_id,content_type='jpg' or 'png'):
        if Chat.query.filter_by(Chat.chat_id == chat_id).first():
            return Content.query.filter_by(content_type = Content_type)


    @staticmethod
    def upload_media():
        return 
    
    