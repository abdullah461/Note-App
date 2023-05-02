from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# creating database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    # the secret key secure the cookies and session data
    app.config['SECRET_KEY'] = 'abdullahi'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # innitialize our database
    db.init_app(app)

    from .views import views
    from .auth import auth

    # registering our blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note

    with app.app_context():
        db.create_all()

    return app