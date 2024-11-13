from shared.models.chat_model import Content
from dm_app.Services.chat_service import ChatService
from shared.utils.db_utils import db
import firebase_admin 
from firebase_admin import credentials, storage
import tkinter as tk
from tkinter import filedialog
import os

class CloudService:
    # init firebase
    cred = credentials.Certificate('social-media-app-9c28f-firebase-adminsdk-yx5k3-72b98152fe.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'social-media-app-9c28f.appspot.com'
    })


    @staticmethod
    def upload_media_(file_path, destination_path,chat_id):
        
        #init bucket
        bucket = storage.bucket()

        blob = bucket.blob(destination_path)

        blob.upload_from_filename(file_path)

        content = Content(chat_id=chat_id, content_type=os.path.splitext(file_path)[-1], content_url=ChatService.chat_encryption(blob.public_url))

        db.session.add(content)
        db.session.commit()

        return blob.public_url

    # @staticmethod
    # def get_uploaded_file_url(destination_path):

    #     bucket = storage.bucket()
        
    #     blob = bucket.blob(destination_path)
        
    #     return blob.public_url


    @staticmethod
    def select_file_dialog(chat_id):

        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Select a File to send.")

        if file_path:
            destination_path = 'Media_Files/' + os.path.basename(file_path)

            public_url = CloudService.upload_media_(file_path, destination_path,chat_id)
            return public_url
        else:
            return 0