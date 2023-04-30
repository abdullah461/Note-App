from flask import Flask

def create_app():
    app = Flask(__name__)
    # the secret key secure the cookies and session data
    app.config['SECRET_KEY'] = 'abdullahi'

    return app