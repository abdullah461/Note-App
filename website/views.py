from flask import Blueprint, render_template
from flask_login import login_required, current_user

# blue print simply means all the routes are
# inside it in this file

views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html")
