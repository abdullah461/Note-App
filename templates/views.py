from flask import Blueprint

# blue print simply means all the routes are
# inside it in this file

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return "<h1>Hello world</h1>"
