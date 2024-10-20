import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from post_app.routes.post_routes import post_bp
from shared.utils.db_utils import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Joseph.reso812345@localhost/social_media_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(post_bp)

@app.route('/')
def home():
    return "<h1> 🥳 Post_app chal rha h..</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5002)
