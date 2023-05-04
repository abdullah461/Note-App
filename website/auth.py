from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
# flash paackage is used when you want to flash some message on the screen

# we use request package to get request of data from the form

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
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 character', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 2 character', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 character', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        else:
            # add user to database
            new_user = User(email=email, first_name=first_name, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")
