from flask import Flask

def create_app():
    app = Flask(__name__)
    # the secret key secure the cookies and session data
    app.config['SECRET_KEY'] = 'abdullahi'

    from .views import views
    from .auth import auth
    # registering our blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
      
    return app