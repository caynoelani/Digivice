#******************************************************
#***********************IMPORTS************************
#******************************************************

#=====================================
# Import app
#=====================================
from flask_app import app

#=====================================
# Import Modules/Packages
#=====================================
from flask import redirect, render_template, session, request, flash, url_for
import functools
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#=====================================
# Import Models
#=====================================
from flask_app.models import user_model


#******************************************************
#**********************Decorators**********************
#******************************************************

#=====================================
# Login Required Decorator
#=====================================
def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' in session:
            return func(*args, **kwargs)
        else:
            flash("Please login")
            return redirect(url_for('login_page'))
    return wrapper


#******************************************************
#***********************ROUTES*************************
#******************************************************

#=====================================
# Login/Register Route (GET)
#=====================================
@app.route('/login')
def login_page():
        is_logged_in = user_model.User.validate_logged_in()

        if is_logged_in:
            return redirect('/favorites')

        return render_template('login.html', is_logged_in = is_logged_in)

#=====================================
# Login/Register Route (POST)
#=====================================
@app.route('/login', methods=["POST"])
def login_post():

    if request.form["form_type"] == "login":
        if not user_model.User.validate_login(request.form):
            return redirect ('/login')

        data = { "email" : request.form["email"] }
        user = user_model.User.get_user_by_email(data)

        session["user_id"] = user.id
        session["username"] = user.username

    elif request.form["form_type"] == "register":
        if not user_model.User.validate_register(request.form):
            return redirect ('/login')

        pw_hash = bcrypt.generate_password_hash(request.form['password'])

        data = {
            "username" : request.form['username'],
            "email" : request.form['email'],
            "password" : pw_hash
        }

        user_id = user_model.User.create_user(data)

        session['user_id'] = user_id
        session["username"] = request.form["username"]

    return redirect('/favorites')

#=====================================
# Logout Route
#=====================================
@app.route('/logout')
@login_required
def logout():
    
    session.clear()
    return redirect(url_for('login_page'))