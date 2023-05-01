from flask import Blueprint, render_template

# blue print simply means all the routes are
# inside it in this file

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")
