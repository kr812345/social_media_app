from flask import Blueprint, redirect, url_for
from user_app.controllers.user_controller import UserController
from dm_app.Routes.Chat_routes import chat_bp

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['GET'])
def users_home():
            return f"User App<a style='color: #53ed98; text-decoration: none; margin: 20px; padding: 15px; border-radius:10px; border: #53ed98 2px solid;' href={'/api/users'}> get_all_users 😎</a> <a style='color: #53ed98; text-decoration: none; margin: 10px; padding: 15px; border-radius:10px; border: #53ed98 2px solid;' href={"/api/users/<username"}> get_user 🫠</a> <a style='color: #53ed98; text-decoration: none; margin: 10px; padding: 15px; border-radius:10px; border: #53ed98 2px solid;' href='/redirect'> Open Chat App 🫠</a>"

@chat_bp.route('/redirect')
def redirect():
    return redirect(url_for(get_all_chats))

@user_bp.route('/api/users', methods=['GET'])
def get_all_users():
    print("ss")
    return UserController.get_all_users()

@user_bp.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    return UserController.get_user(username)

@user_bp.route('/api/users', methods=['POST'])
def create_user():
    return UserController.create_user()

@user_bp.route('/api/users/login', methods=['POST'])
def login_user():
    return UserController.login_user()
