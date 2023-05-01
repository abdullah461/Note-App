from flask import Blueprint, render_template

# blue print simply means all the routes are
# inside it in this file

auth = Blueprint('auth',__name__)
    
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="testing")

@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html")
