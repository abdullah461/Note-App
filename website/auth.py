from flask import Blueprint, render_template, request, flash

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
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 character', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 character', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 character', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        else:
            flash('Account created!', category='success')
            # add user to database
    return render_template("sign_up.html")
