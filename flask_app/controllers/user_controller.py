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
from flask import redirect, render_template, session, request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#=====================================
# Import Models
#=====================================
from flask_app.models import user_model

#******************************************************
#***********************ROUTES*************************
#******************************************************

#=====================================
# Login Routes
#=====================================
@app.route('/login')
def render_login():

    is_logged_in = user_model.User.validate_logged_in()

    if is_logged_in:
        return redirect('/favorites')

    return render_template('login.html', is_logged_in = is_logged_in)

@app.route('/login', methods=["POST"])
def user_login():
    
    if request.form["form_type"] == "login":
        if not user_model.User.validate_login(request.form):
            return redirect ('/login')

        data = { "email" : request.form["email"] }
        user = user_model.User.get_by_email(data)

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

        user_id = user_model.User.create(data)

        session['user_id'] = user_id
        session["username"] = request.form["username"]

    return redirect('/favorites')

#=====================================
# Logout Route
#=====================================
@app.route('/logout')
def logout():
    
    session.clear()
    return redirect('/')